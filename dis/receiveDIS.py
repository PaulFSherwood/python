#!/usr/bin/env python3
"""
Minimal DIS UDP analyzer for Linux/Windows with no third-party libraries.
Understands only:
  - 1: Entity State PDU
  - 2: Fire PDU
  - 3: Detonation PDU

Tested conceptually against a simple sender that emits DIS v7-style headers.
"""

from __future__ import annotations

import argparse
import signal
import socket
import struct
import sys
import time
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

# DIS common header: protocolVersion, exerciseID, pduType, protocolFamily,
# timestamp, length, pduStatus, padding
HEADER_FMT = ">BBBBIHBB"
HEADER_LEN = struct.calcsize(HEADER_FMT)

# Common DIS entity identifier: site, application, entity
ENTITY_ID_FMT = ">HHH"
ENTITY_ID_LEN = struct.calcsize(ENTITY_ID_FMT)

PDU_NAMES = {
    1: "EntityState",
    2: "Fire",
    3: "Detonation",
}


@dataclass
class Header:
    protocol_version: int
    exercise_id: int
    pdu_type: int
    protocol_family: int
    timestamp: int
    length: int
    pdu_status: int
    padding: int


@dataclass
class EntityStateRecord:
    entity_id: Tuple[int, int, int]
    force_id: int
    marking: str
    location: Tuple[float, float, float]
    orientation: Tuple[float, float, float]


@dataclass
class FireRecord:
    firing_entity: Tuple[int, int, int]
    target_entity: Tuple[int, int, int]
    munition_entity: Tuple[int, int, int]
    event_id: Tuple[int, int, int]


@dataclass
class DetonationRecord:
    firing_entity: Tuple[int, int, int]
    target_entity: Tuple[int, int, int]
    exploding_entity: Tuple[int, int, int]
    event_id: Tuple[int, int, int]


class AnalyzerState:
    def __init__(self) -> None:
        self.packet_count = 0
        self.byte_count = 0
        self.by_pdu: Dict[int, int] = {}
        self.entities: Dict[Tuple[int, int, int], EntityStateRecord] = {}
        self.last_fire_by_event: Dict[Tuple[int, int, int], FireRecord] = {}
        self.start_time = time.time()

    def bump(self, pdu_type: int, packet_len: int) -> None:
        self.packet_count += 1
        self.byte_count += packet_len
        self.by_pdu[pdu_type] = self.by_pdu.get(pdu_type, 0) + 1

    def print_summary(self) -> None:
        elapsed = max(time.time() - self.start_time, 0.001)
        print("\n=== DIS SUMMARY ===")
        print(f"uptime_s      : {elapsed:.1f}")
        print(f"packets       : {self.packet_count}")
        print(f"bytes         : {self.byte_count}")
        print(f"packets_per_s : {self.packet_count / elapsed:.2f}")
        print(f"tracked_entities: {len(self.entities)}")
        for pdu_type in sorted(self.by_pdu):
            print(f"{PDU_NAMES.get(pdu_type, f'PDU-{pdu_type}'):>12}: {self.by_pdu[pdu_type]}")
        print()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Minimal DIS UDP analyzer")
    parser.add_argument("--host", default="0.0.0.0", help="Bind address")
    parser.add_argument("--port", type=int, default=3000, help="UDP port to listen on")
    parser.add_argument(
        "--only",
        choices=["entity", "fire", "detonation", "all"],
        default="all",
        help="Only print one PDU class",
    )
    parser.add_argument(
        "--entity",
        metavar="SITE:APP:ENT",
        help="Only print packets involving this entity ID",
    )
    parser.add_argument(
        "--summary-every",
        type=float,
        default=10.0,
        help="Print counters every N seconds; 0 disables periodic summary",
    )
    parser.add_argument(
        "--quiet-entity-state",
        action="store_true",
        help="Track Entity State PDUs but do not print each one",
    )
    return parser.parse_args()


def parse_entity_filter(text: Optional[str]) -> Optional[Tuple[int, int, int]]:
    if not text:
        return None
    parts = text.split(":")
    if len(parts) != 3:
        raise SystemExit("--entity must look like SITE:APP:ENT, example 1:100:3")
    return int(parts[0]), int(parts[1]), int(parts[2])


def parse_header(data: bytes) -> Optional[Header]:
    if len(data) < HEADER_LEN:
        return None
    values = struct.unpack_from(HEADER_FMT, data, 0)
    return Header(*values)


def parse_entity_id(data: bytes, offset: int) -> Tuple[int, int, int]:
    return struct.unpack_from(ENTITY_ID_FMT, data, offset)


def parse_entity_state(data: bytes) -> EntityStateRecord:
    # Offsets assume standard Entity State PDU layout.
    entity_id = parse_entity_id(data, 12)
    force_id = data[18]
    x, y, z = struct.unpack_from(">ddd", data, 48)
    psi, theta, phi = struct.unpack_from(">fff", data, 72)
    raw_marking = data[129:140]
    marking = raw_marking.split(b"\x00", 1)[0].decode("ascii", errors="replace").strip()
    return EntityStateRecord(
        entity_id=entity_id,
        force_id=force_id,
        marking=marking,
        location=(x, y, z),
        orientation=(psi, theta, phi),
    )


def parse_fire(data: bytes) -> FireRecord:
    firing_entity = parse_entity_id(data, 12)
    target_entity = parse_entity_id(data, 18)
    munition_entity = parse_entity_id(data, 24)
    event_id = parse_entity_id(data, 30)
    return FireRecord(
        firing_entity=firing_entity,
        target_entity=target_entity,
        munition_entity=munition_entity,
        event_id=event_id,
    )


def parse_detonation(data: bytes) -> DetonationRecord:
    firing_entity = parse_entity_id(data, 12)
    target_entity = parse_entity_id(data, 18)
    exploding_entity = parse_entity_id(data, 24)
    event_id = parse_entity_id(data, 30)
    return DetonationRecord(
        firing_entity=firing_entity,
        target_entity=target_entity,
        exploding_entity=exploding_entity,
        event_id=event_id,
    )


def record_matches_entity(record, entity_filter: Optional[Tuple[int, int, int]]) -> bool:
    if entity_filter is None:
        return True

    if isinstance(record, EntityStateRecord):
        return record.entity_id == entity_filter

    if isinstance(record, FireRecord):
        return entity_filter in (
            record.firing_entity,
            record.target_entity,
            record.munition_entity,
        )

    if isinstance(record, DetonationRecord):
        return entity_filter in (
            record.firing_entity,
            record.target_entity,
            record.exploding_entity,
        )

    return False


def should_print_pdu(pdu_type: int, only: str) -> bool:
    if only == "all":
        return True
    if only == "entity":
        return pdu_type == 1
    if only == "fire":
        return pdu_type == 2
    if only == "detonation":
        return pdu_type == 3
    return True


def format_eid(eid: Tuple[int, int, int]) -> str:
    return f"{eid[0]}:{eid[1]}:{eid[2]}"


def print_entity_state(record: EntityStateRecord) -> None:
    x, y, z = record.location
    psi, theta, phi = record.orientation
    mark = f" {record.marking}" if record.marking else ""
    print(
        f"ES  entity={format_eid(record.entity_id)} force={record.force_id}{mark} "
        f"loc=({x:.1f},{y:.1f},{z:.1f}) ori=({psi:.3f},{theta:.3f},{phi:.3f})"
    )


def print_fire(record: FireRecord) -> None:
    print(
        f"FI  event={format_eid(record.event_id)} shooter={format_eid(record.firing_entity)} "
        f"target={format_eid(record.target_entity)} munition={format_eid(record.munition_entity)}"
    )


def print_detonation(record: DetonationRecord, state: AnalyzerState) -> None:
    prefix = (
        f"DE  event={format_eid(record.event_id)} shooter={format_eid(record.firing_entity)} "
        f"target={format_eid(record.target_entity)} exploding={format_eid(record.exploding_entity)}"
    )
    matched_fire = state.last_fire_by_event.get(record.event_id)
    if matched_fire:
        prefix += " matched_fire=yes"
    print(prefix)


def main() -> int:
    args = parse_args()
    entity_filter = parse_entity_filter(args.entity)
    state = AnalyzerState()
    next_summary = time.time() + args.summary_every if args.summary_every > 0 else 0.0

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((args.host, args.port))

    def handle_sigint(signum, frame):  # type: ignore[unused-argument]
        state.print_summary()
        raise SystemExit(0)

    signal.signal(signal.SIGINT, handle_sigint)

    print(f"Listening for DIS UDP on {args.host}:{args.port}")
    print("Ctrl+C prints a summary and exits.\n")

    while True:
        data, addr = sock.recvfrom(65535)
        header = parse_header(data)
        if header is None:
            continue

        state.bump(header.pdu_type, len(data))

        try:
            if header.pdu_type == 1:
                if len(data) < 144:
                    continue
                record = parse_entity_state(data)
                state.entities[record.entity_id] = record
                if should_print_pdu(1, args.only) and record_matches_entity(record, entity_filter):
                    if not args.quiet_entity_state:
                        print_entity_state(record)

            elif header.pdu_type == 2:
                if len(data) < 36:
                    continue
                record = parse_fire(data)
                state.last_fire_by_event[record.event_id] = record
                if should_print_pdu(2, args.only) and record_matches_entity(record, entity_filter):
                    print_fire(record)

            elif header.pdu_type == 3:
                if len(data) < 36:
                    continue
                record = parse_detonation(data)
                if should_print_pdu(3, args.only) and record_matches_entity(record, entity_filter):
                    print_detonation(record, state)

            else:
                if should_print_pdu(header.pdu_type, args.only):
                    name = PDU_NAMES.get(header.pdu_type, f"PDU-{header.pdu_type}")
                    print(
                        f"{name} from {addr[0]}:{addr[1]} len={header.length} "
                        f"exercise={header.exercise_id} family={header.protocol_family}"
                    )

        except struct.error as exc:
            print(f"Parse error for PDU type {header.pdu_type}: {exc}", file=sys.stderr)

        if args.summary_every > 0 and time.time() >= next_summary:
            state.print_summary()
            next_summary = time.time() + args.summary_every


if __name__ == "__main__":
    raise SystemExit(main())
