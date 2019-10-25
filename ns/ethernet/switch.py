from ns.ethernet.frame import EthernetFrame
from ns.ethernet.node import Node

from ns.mac import BROADCAST_MAC_ADDRESS

class Switch(Node):
  def __init__(self, mac_addr, num_of_ports):
    super().__init__(mac_addr = mac_addr, broadcast_domain = None)
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
    if frame.dest_mac_addr == BROADCAST_MAC_ADDRESS:
      self.broadcast(frame)
    else:
      self.send(frame)

  def send(self, frame):
    try:
      node = self._connected_nodes[frame.dest_mac_addr]
      if frame.broadcast_domain is None or frame.broadcast_domain == node.broadcast_domain:
        node.receive(frame)
      else:
        print('Node {} is of a separate broadcast domain {} and cannot receive a message {}.'.format(node.mac_addr, 
                                                                                                     node.broadcast_domain, 
                                                                                                     frame))
    except KeyError:
      print('There is no recipient for the packet {}'.format(frame)) 


  def broadcast(self, frame):
    db_comparer = lambda frame, node: ((frame.broadcast_domain is None and node.broadcast_domain is None) or
                                        frame.broadcast_domain == node.broadcast_domain)
    broadcast_nodes = [node for node in self._connected_nodes.values() if db_comparer(frame, node) and 
                                                                          node.mac_addr != frame.source_mac_addr]
    for node in broadcast_nodes:
      node.receive(frame)

  def __repr__(self):
    return "Switch {} with {} open ports out of {}. Mac Address Table {}".format(self.mac_addr, 
                                                                                 self.open_ports,
                                                                                 self.num_of_ports,
                                                                                 self.mac_addr_table)