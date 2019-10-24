from ns.ethernet.node import Node

class Router(Node):
  def __init__(self, mac_addr):
    super().__init__(mac_addr = mac_addr)