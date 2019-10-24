from ns.ethernet.frame import EthernetFrame
from ns.mac import BROADCAST_MAC_ADDRESS

class Node:
  def __init__(self, mac_addr):
    self._mac_addr = mac_addr
    self._connected_nodes = { mac_addr: self }

  def get_type(self):
    return "node"

  @property
  def mac_addr(self):
    return self._mac_addr
  
  @mac_addr.setter
  def mac_addr(self, value):
    raise PermissionError('MAC address cannot be changed!')

  def _send_to_switch(self, message, to_mac):
    switches = [sw for sw in self._connected_nodes.values() if sw.get_type() == 'switch']
    for sw in switches:
      frame = EthernetFrame(self.mac_addr, to_mac, 'IPv4', message)
      sw.receive(frame)

  def connect(self, node):
    self._connected_nodes[node.mac_addr] = node

  def send(self, message, to_mac):
    frame = EthernetFrame(self.mac_addr, to_mac, 'IPv4', message)
    try:
      self._connected_nodes[to_mac].receive(frame)
    except KeyError:
      self._send_to_switch(message, to_mac)

  def broadcast(self, message):
    for node_mac in self._connected_nodes.keys():
      frame = EthernetFrame(self.mac_addr, BROADCAST_MAC_ADDRESS, 'IPv4', message)
      self._connected_nodes[node_mac].receive(frame)

  def receive(self, frame):
    print('Node {} received a message "{}" from node {}'.format(self.mac_addr, frame.data, frame.source_mac_addr))

  def __repr__(self):
    return "Node '{}'. Connected to '{}'".format(self.mac_addr, self._connected_nodes.keys)