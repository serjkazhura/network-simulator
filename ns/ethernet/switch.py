from ns.ethernet.node import Node

class Switch(Node):
  def __init__(self, mac_addr, num_of_ports):
    super().__init__(mac_addr = mac_addr)
    self.mac_addr_table = {0: None} # doing a 1 based dictionary here
    self.open_ports = num_of_ports
  
  def connect(self, node):
    if self.open_ports == 0:
      raise ValueError("All the ports are exausted.")

    super().connect(node)
    self.mac_addr_table[self.open_ports] = node.mac_addr
    self.open_ports -= 1

  def __repr__(self):
    return "Switch {} with {} open ports. Connected to {}. Mac Address Table {}".format(self.mac_addr, 
                                                                                        self.open_ports,
                                                                                        self._connected_nodes,
                                                                                        self.mac_addr_table)