import tkinter as tk
from dataclasses import dataclass

# =========================
# I2C BUS SIMULATION
# =========================

class I2CBus:
    def __init__(self):
        self.receivers = {}

    def register_receiver(self, node_id, callback):
        self.receivers[node_id] = callback

    def send(self, dest_id, packet):
        if dest_id in self.receivers:
            self.receivers[dest_id](packet)
        else:
            print(f"[BUS] No receiver with ID {dest_id}")

BUS = I2CBus()

# =========================
# DATA PACKET
# =========================

@dataclass
class I2CPacket:
    src_id: int
    switches: list
    message: str

# =========================
# SENDER WINDOW
# =========================

class SenderWindow:
    def __init__(self, master):
        self.win = tk.Toplevel(master)
        self.win.title("I2C Sender")

        self.switches = [tk.IntVar() for _ in range(4)]

        top = tk.Frame(self.win)
        top.pack(pady=5)

        for i, v in enumerate(self.switches):
            tk.Checkbutton(top, text=f"S{i}", variable=v).pack(side=tk.LEFT)

        mid = tk.Frame(self.win)
        mid.pack(pady=5)

        tk.Label(mid, text="Message").pack(anchor="w")
        self.msg_entry = tk.Entry(mid, width=40)
        self.msg_entry.pack()

        bottom = tk.Frame(self.win)
        bottom.pack(pady=5)

        tk.Label(bottom, text="Dest ID").pack(side=tk.LEFT)
        self.dest_entry = tk.Entry(bottom, width=5)
        self.dest_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(bottom, text="Src ID").pack(side=tk.LEFT)
        self.src_entry = tk.Entry(bottom, width=5)
        self.src_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(self.win, text="Send", command=self.send).pack(pady=5)

    def send(self):
        try:
            dest = int(self.dest_entry.get())
            src = int(self.src_entry.get())
        except ValueError:
            return

        packet = I2CPacket(
            src_id=src,
            switches=[v.get() for v in self.switches],
            message=self.msg_entry.get()
        )

        BUS.send(dest, packet)

# =========================
# RECEIVER PANEL
# =========================

class ReceiverPanel(tk.Frame):
    def __init__(self, master, node_id):
        super().__init__(master, relief=tk.RIDGE, borderwidth=2)
        self.node_id = node_id

        header = tk.Frame(self)
        header.pack(anchor="w")

        tk.Label(header, text="Receiver ID:").pack(side=tk.LEFT)
        self.id_label = tk.Label(header, text=str(node_id))
        self.id_label.pack(side=tk.LEFT)

        self.meta = tk.Label(self, text="From Src ID: - → Dest ID: -")
        self.meta.pack(anchor="w")

        self.switch_labels = []
        row = tk.Frame(self)
        row.pack(anchor="w")

        for i in range(4):
            lbl = tk.Label(row, text="0", width=3, relief=tk.SUNKEN)
            lbl.pack(side=tk.LEFT, padx=2)
            self.switch_labels.append(lbl)

        self.text = tk.Text(self, height=3, width=40)
        self.text.pack(pady=2)

        BUS.register_receiver(node_id, self.receive)

    def receive(self, packet: I2CPacket):
        self.meta.config(
            text=f"From Src ID: {packet.src_id} → Dest ID: {self.node_id}"
        )

        for i, v in enumerate(packet.switches):
            self.switch_labels[i].config(text=str(v))

        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, packet.message)

# =========================
# RECEIVER WINDOW
# =========================

class ReceiverWindow:
    def __init__(self, master):
        self.win = tk.Toplevel(master)
        self.win.title("I2C Receiver")

        top = tk.Frame(self.win)
        top.pack(pady=5)

        tk.Label(top, text="Receiver ID").pack(side=tk.LEFT)

        self.id_entry = tk.Entry(top, width=5)
        self.id_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(top, text="Add", command=self.add_receiver).pack(side=tk.LEFT)

        self.container = tk.Frame(self.win)
        self.container.pack(pady=5)

    def add_receiver(self):
        try:
            node_id = int(self.id_entry.get())
        except ValueError:
            return

        if node_id in BUS.receivers:
            return

        panel = ReceiverPanel(self.container, node_id)
        panel.pack(pady=5, fill=tk.X)

# =========================
# MAIN APP
# =========================

class MainApp:
    def __init__(self, root):
        root.title("I2C Simulator")

        tk.Button(root, text="Add Sender", command=lambda: SenderWindow(root)).pack(pady=5)
        tk.Button(root, text="Add Receiver", command=lambda: ReceiverWindow(root)).pack(pady=5)

root = tk.Tk()
MainApp(root)
root.mainloop()
