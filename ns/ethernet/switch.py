from ns.ethernet.node import Node

class Switch(Node):
  def __init__(self, mac_addr):
    super().__init__(mac_addr = mac_addr)