from ns.ethernet.frame import EthernetFrame
from ns.mac import BROADCAST_MAC_ADDRESS

class Node:
  def __init__(self, mac_addr):
    self._mac_addr = mac_addr
    self._connected_nodes = { mac_addr: self }
    self._connected_routers = {}
    self._connected_switches = {}

  def get_type(self):
    return "node"

  @property
  def mac_addr(self):
    return self._mac_addr
  
  @mac_addr.setter
  def mac_addr(self, value):
    raise PermissionError('MAC address cannot be changed!')

  def _send_to_node(self, message, to_mac):
    frame = EthernetFrame(self.mac_addr, to_mac, 'IPv4', message)
    try:
      self._connected_nodes[to_mac].receive(frame)
    except KeyError:
      print('Node {} is not connected to {} directly.'.format(to_mac, self.mac_addr))

  def _send_to_switch(self, message, to_mac):
    for sw in self._connected_switches.values():
      frame = EthernetFrame(self.mac_addr, to_mac, 'IPv4', message)
      sw.receive(frame)

  def connect(self, node):
    if (node.get_type() == 'node'):
      self._connected_nodes[node.mac_addr] = node
    elif (node.get_type() == 'switch'):
      self._connected_switches[node.mac_addr] = node
    elif (node.get_type() == 'router'):
      self._connected_routers[node.mac_addr] = node
    else:
      raise ValueError('Unknown device!')

  def send(self, message, to_mac):
    self._send_to_switch(message, to_mac)
    self._send_to_node(message, to_mac)

  def broadcast(self, message):
    for node_mac in self._connected_nodes.keys():
      frame = EthernetFrame(self.mac_addr, BROADCAST_MAC_ADDRESS, 'IPv4', message)
      self._connected_nodes[node_mac].receive(frame)

  def receive(self, frame):
    print('{} {} received a message "{}" from node {}'.format(self.get_type().title(), 
                                                              self.mac_addr, 
                                                              frame.data, 
                                                              frame.source_mac_addr))

  def __repr__(self):
    return "Node '{}'. Connected to '{}'".format(self.mac_addr, self._connected_nodes.keys)