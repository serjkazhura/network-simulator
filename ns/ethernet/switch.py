from ns.ethernet.frame import EthernetFrame
from ns.ethernet.node import Node

class Switch(Node):
  def __init__(self, mac_addr, num_of_ports):
    super().__init__(mac_addr = mac_addr)
    self.mac_addr_table = {}
    self.open_ports = num_of_ports
    self.num_of_ports = num_of_ports

  def get_type(self):
    return "switch"

  def connect(self, node):
    if self.open_ports == 0:
      raise ValueError("All the ports are exausted.")

    super().connect(node)
    self.mac_addr_table[node.mac_addr] = self.open_ports
    self.open_ports -= 1

  def receive(self, frame):
    super().receive(frame)
    if frame.dest_mac_addr == self.mac_addr:
      return
    try:
      # dest_mac = self.mac_addr_table[frame.dest_mac_addr]
      self._connected_nodes[frame.dest_mac_addr].receive(frame)
    except KeyError:
      print('There is no recipient for the packet {}'.format(frame)) 

  def __repr__(self):
    return "Switch {} with {} open ports out of {}. Mac Address Table {}".format(self.mac_addr, 
                                                                                 self.open_ports,
                                                                                 self.num_of_ports,
                                                                                 self.mac_addr_table)