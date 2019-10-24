class Node:
  def __init__(self, mac_addr):
    self._mac_addr = mac_addr
    self._connected_nodes = set()

  @property
  def mac_addr(self):
    return self._mac_addr
  
  @mac_addr.setter
  def mac_addr(self, value):
    raise PermissionError('MAC address cannot be changed!')

  def connect(self, node):
    self._connected_nodes.add(node.mac_addr)

  def __repr__(self):
    return "Node '{}'. Connected to '{}'".format(self.mac_addr, self._connected_nodes)