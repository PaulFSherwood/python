#!/usr/bin/env python3
import math
import random
import socket
import time
from dataclasses import dataclass
from io import BytesIO

from opendis.DataOutputStream import DataOutputStream
from opendis.DataInputStream import DataInputStream

# from opendis.stream import DataOutputStream
from opendis.dis7 import (
    EntityStatePdu,
    FirePdu,
    DetonationPdu,
    EntityType,
    MunitionDescriptor,
    EventIdentifier,
    Vector3Float,
)
from opendis.RangeCoordinates import GPS, deg2rad

DESTINATION_IP = "127.0.0.1"
DESTINATION_PORT = 3000

# For testing, set this to 15 or 30.
ATTACK_INTERVAL_SECONDS = 15
DET_DELAY_SECONDS = 2.0
STATE_RATE_HZ = 1.0

# Pick any convenient anchor point.
# The sim moves in a local flat world, then converts to DIS world coordinates.
ANCHOR_LAT_DEG = 35.0844
ANCHOR_LON_DEG = -106.6504
EARTH_RADIUS_M = 6378137.0

gps = GPS()


@dataclass
class FakeEntity:
    site: int
    app: int
    ent: int
    name: str
    force_id: int
    country: int
    domain: str     # "land" or "air"
    east_m: float
    north_m: float
    altitude_m: float
    circle_radius_m: float
    angular_speed_deg_s: float
    angle_deg: float
    heading_deg: float = 0.0
    alive: bool = True


WEAPONS = [
    # These EntityType values are placeholders for analyzer traffic generation.
    # Tighten them later with the exact SISO EBV values you want.
    {
        "name": "bullet",
        "speed_m_s": 900.0,
        "descriptor": dict(entityKind=2, domain=0, category=1, subcategory=1, specific=1, extra=0),
        "det_result": 1,
    },
    {
        "name": "missile_short",
        "speed_m_s": 600.0,
        "descriptor": dict(entityKind=2, domain=0, category=2, subcategory=1, specific=1, extra=0),
        "det_result": 1,
    },
    {
        "name": "missile_long",
        "speed_m_s": 1000.0,
        "descriptor": dict(entityKind=2, domain=0, category=2, subcategory=2, specific=1, extra=0),
        "det_result": 1,
    },
]

def init_pdu_header(pdu, exercise_id: int = 1):
    pdu.exerciseID = exercise_id
    pdu.timestamp = 0
    pdu.pduStatus = 0
    pdu.padding = 0

def local_to_lat_lon(anchor_lat_deg: float, anchor_lon_deg: float, east_m: float, north_m: float):
    lat_rad = math.radians(anchor_lat_deg)
    dlat = north_m / EARTH_RADIUS_M
    dlon = east_m / (EARTH_RADIUS_M * math.cos(lat_rad))
    lat = anchor_lat_deg + math.degrees(dlat)
    lon = anchor_lon_deg + math.degrees(dlon)
    return lat, lon


def lla_to_ecef_with_orientation(lat_deg: float, lon_deg: float, alt_m: float, yaw_deg: float):
    # The Open-DIS example sender uses GPS.llarpy2ecef() for this conversion.
    return gps.llarpy2ecef(
        deg2rad(lat_deg),
        deg2rad(lon_deg),
        alt_m,
        0.0,
        0.0,
        deg2rad(yaw_deg),
    )


def set_entity_identifier(obj, site: int, app: int, ent: int):
    if hasattr(obj, "simulationAddress"):
        obj.simulationAddress.site          = site
        obj.simulationAddress.application   = app
        obj.entityNumber                    = ent
    else:
        obj.siteID          = site
        obj.applicationID   = app
        obj.entityID        = ent

def serialize_pdu(pdu) -> bytes:
    memory_stream = BytesIO()
    output_stream = DataOutputStream(memory_stream)
    pdu.serialize(output_stream)
    return memory_stream.getvalue()


def build_entity_type(entity: FakeEntity) -> EntityType:
    et = EntityType()
    et.entityKind = 1  # platform
    et.country = entity.country

    if entity.domain == "land":
        et.domain = 1
        et.category = 1
        et.subcategory = 1
        et.specific = 1
        et.extra = 0
    else:
        et.domain = 2
        et.category = 1
        et.subcategory = 1
        et.specific = 1
        et.extra = 0

    return et

def build_entity_state_pdu(entity: FakeEntity) -> EntityStatePdu:
    lat_deg, lon_deg = local_to_lat_lon(
        ANCHOR_LAT_DEG, ANCHOR_LON_DEG, entity.east_m, entity.north_m
    )
    ecef = lla_to_ecef_with_orientation(lat_deg, lon_deg, entity.altitude_m, entity.heading_deg)

    pdu = EntityStatePdu()
    init_pdu_header(pdu)
    pdu.pduType = 1

    set_entity_identifier(pdu.entityID, entity.site, entity.app, entity.ent)
    pdu.forceId = entity.force_id
    pdu.entityType = build_entity_type(entity)
    pdu.marking.setString(entity.name[:11])

    pdu.entityLocation.x = ecef[0]
    pdu.entityLocation.y = ecef[1]
    pdu.entityLocation.z = ecef[2]

    pdu.entityOrientation.psi = ecef[3]
    pdu.entityOrientation.theta = ecef[4]
    pdu.entityOrientation.phi = ecef[5]

    pdu.entityLinearVelocity.x = 0.0
    pdu.entityLinearVelocity.y = 0.0
    pdu.entityLinearVelocity.z = 0.0

    pdu.entityAppearance = 0
    pdu.deadReckoningAlgorithm = 0
    pdu.capabilities = 0

    pdu.deadReckoningParameters.entityLinearAcceleration.x = 0.0
    pdu.deadReckoningParameters.entityLinearAcceleration.y = 0.0
    pdu.deadReckoningParameters.entityLinearAcceleration.z = 0.0

    pdu.deadReckoningParameters.entityAngularVelocity.x = 0.0
    pdu.deadReckoningParameters.entityAngularVelocity.y = 0.0
    pdu.deadReckoningParameters.entityAngularVelocity.z = 0.0

    return pdu

def build_munition_descriptor(shooter: FakeEntity, weapon_cfg: dict) -> MunitionDescriptor:
    md = MunitionDescriptor()
    md.quantity = 1
    md.rate = 0
    md.warhead = 1
    md.fuse = 1
    md.munitionType.entityKind = weapon_cfg["descriptor"]["entityKind"]
    md.munitionType.domain = weapon_cfg["descriptor"]["domain"]
    md.munitionType.country = shooter.country
    md.munitionType.category = weapon_cfg["descriptor"]["category"]
    md.munitionType.subcategory = weapon_cfg["descriptor"]["subcategory"]
    md.munitionType.specific = weapon_cfg["descriptor"]["specific"]
    md.munitionType.extra = weapon_cfg["descriptor"]["extra"]
    return md


def build_event_identifier(shooter: FakeEntity, event_number: int) -> EventIdentifier:
    ev = EventIdentifier()
    ev.simulationAddress.site = shooter.site
    ev.simulationAddress.application = shooter.app
    ev.eventNumber = event_number
    return ev


def build_fire_pdu(shooter: FakeEntity, target: FakeEntity, weapon_cfg: dict, event_number: int) -> FirePdu:
    shooter_lat, shooter_lon = local_to_lat_lon(
        ANCHOR_LAT_DEG, ANCHOR_LON_DEG, shooter.east_m, shooter.north_m
    )
    shooter_ecef = lla_to_ecef_with_orientation(
        shooter_lat, shooter_lon, shooter.altitude_m, shooter.heading_deg
    )

    dx = target.east_m - shooter.east_m
    dy = target.north_m - shooter.north_m
    rng = math.hypot(dx, dy)

    fire = FirePdu()
    init_pdu_header(fire)
    fire.pduType = 2

    set_entity_identifier(fire.firingEntityID, shooter.site, shooter.app, shooter.ent)
    set_entity_identifier(fire.targetEntityID, target.site, target.app, target.ent)
    set_entity_identifier(fire.munitionExpendableID, shooter.site, shooter.app, 5000 + event_number)

    fire.eventID = build_event_identifier(shooter, event_number)
    fire.fireMissionIndex = 1
    fire.location.x = shooter_ecef[0]
    fire.location.y = shooter_ecef[1]
    fire.location.z = shooter_ecef[2]
    fire.descriptor = build_munition_descriptor(shooter, weapon_cfg)
    fire.velocity.x = 0.0
    fire.velocity.y = 0.0
    fire.velocity.z = 0.0
    fire.range = rng

    return fire


def build_detonation_pdu(
    shooter: FakeEntity,
    target: FakeEntity,
    weapon_cfg: dict,
    event_number: int,
    hit: bool = True,
) -> DetonationPdu:
    # Small miss jitter if desired
    miss_east = 0.0 if hit else random.uniform(-25.0, 25.0)
    miss_north = 0.0 if hit else random.uniform(-25.0, 25.0)

    det_east = target.east_m + miss_east
    det_north = target.north_m + miss_north
    det_alt = target.altitude_m

    det_lat, det_lon = local_to_lat_lon(
        ANCHOR_LAT_DEG, ANCHOR_LON_DEG, det_east, det_north
    )
    det_ecef = lla_to_ecef_with_orientation(det_lat, det_lon, det_alt, 0.0)

    det = DetonationPdu()
    init_pdu_header(det)
    det.pduType = 3

    set_entity_identifier(det.firingEntityID, shooter.site, shooter.app, shooter.ent)
    set_entity_identifier(det.targetEntityID, target.site, target.app, target.ent)
    set_entity_identifier(det.explodingEntityID, shooter.site, shooter.app, 5000 + event_number)

    det.eventID = build_event_identifier(shooter, event_number)
    det.location.x = det_ecef[0]
    det.location.y = det_ecef[1]
    det.location.z = det_ecef[2]
    det.descriptor = build_munition_descriptor(shooter, weapon_cfg)
    det.velocity = Vector3Float(0.0, 0.0, 0.0)
    det.locationInEntityCoordinates = Vector3Float(0.0, 0.0, 0.0)
    det.detonationResult = weapon_cfg["det_result"]

    return det


def move_entities(entities, dt: float):
    for e in entities:
        if not e.alive:
            continue

        e.angle_deg = (e.angle_deg + e.angular_speed_deg_s * dt) % 360.0
        a = math.radians(e.angle_deg)

        center_east = round(e.east_m / 1000.0) * 1000.0
        center_north = round(e.north_m / 1000.0) * 1000.0

        e.east_m = center_east + e.circle_radius_m * math.cos(a)
        e.north_m = center_north + e.circle_radius_m * math.sin(a)

        # Tangent heading
        e.heading_deg = (e.angle_deg + 90.0) % 360.0


def hostile_targets(shooter: FakeEntity, entities):
    return [e for e in entities if e.alive and e.country != shooter.country]


def make_entities():
    # Countries are placeholders here.
    countries = [225, 222, 71, 78]
    names = [
        "ALPHA1", "ALPHA2", "BRAVO1", "BRAVO2", "CHARL1",
        "CHARL2", "DELTA1", "DELTA2", "EAGLE1", "EAGLE2"
    ]

    entities = []
    base_positions = [
        (-3000, -2000), (-1000, -2000), (1000, -2000), (3000, -2000),
        (-3000, 2000), (-1000, 2000), (1000, 2000), (3000, 2000),
        (-1500, 5000), (1500, 5000),
    ]

    for i in range(10):
        domain = "land" if i < 6 else "air"
        altitude = 0.0 if domain == "land" else 2500.0 + (i - 6) * 500.0
        radius = 300.0 if domain == "land" else 1500.0
        speed = 4.0 if domain == "land" else 12.0

        entities.append(
            FakeEntity(
                site=1,
                app=100,
                ent=i + 1,
                name=names[i],
                force_id=(i % 4) + 1,
                country=countries[i % 4],
                domain=domain,
                east_m=base_positions[i][0],
                north_m=base_positions[i][1],
                altitude_m=altitude,
                circle_radius_m=radius,
                angular_speed_deg_s=speed,
                angle_deg=(i * 36.0),
            )
        )

    return entities


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    entities = make_entities()
    last_attack = 0.0
    last_state = 0.0
    event_number = 1
    pending_dets = []

    print(f"Sending DIS traffic to udp://{DESTINATION_IP}:{DESTINATION_PORT}")

    while True:
        now = time.time()

        # Update motion
        move_entities(entities, 1.0 / STATE_RATE_HZ)

        # Entity State PDUs
        if now - last_state >= (1.0 / STATE_RATE_HZ):
            for e in entities:
                pdu = build_entity_state_pdu(e)
                sock.sendto(serialize_pdu(pdu), (DESTINATION_IP, DESTINATION_PORT))
            last_state = now

        # Fire event
        if now - last_attack >= ATTACK_INTERVAL_SECONDS:
            shooter = random.choice([e for e in entities if e.alive])
            candidates = hostile_targets(shooter, entities)
            if candidates:
                target = random.choice(candidates)
                weapon = random.choice(WEAPONS)

                fire = build_fire_pdu(shooter, target, weapon, event_number)
                sock.sendto(serialize_pdu(fire), (DESTINATION_IP, DESTINATION_PORT))

                pending_dets.append(
                    {
                        "send_at": now + DET_DELAY_SECONDS,
                        "shooter": shooter,
                        "target": target,
                        "weapon": weapon,
                        "event_number": event_number,
                    }
                )

                print(
                    f"FIRE  event={event_number:04d} "
                    f"{shooter.name}->{target.name} weapon={weapon['name']}"
                )
                event_number += 1
            last_attack = now

        # Detonations
        ready = [x for x in pending_dets if x["send_at"] <= now]
        pending_dets = [x for x in pending_dets if x["send_at"] > now]

        for item in ready:
            hit = random.random() < 0.70
            det = build_detonation_pdu(
                item["shooter"],
                item["target"],
                item["weapon"],
                item["event_number"],
                hit=hit,
            )
            sock.sendto(serialize_pdu(det), (DESTINATION_IP, DESTINATION_PORT))
            print(
                f"DETONATION event={item['event_number']:04d} "
                f"target={item['target'].name} hit={hit}"
            )

        time.sleep(0.01)


if __name__ == "__main__":
    main()
