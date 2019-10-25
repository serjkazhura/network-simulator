class EthernetFrame:
  def __init__(self, source_mac_addr, dest_mac_addr, f_type, data, broadcast_domain):
    self.source_mac_addr = source_mac_addr
    self.dest_mac_addr = dest_mac_addr
    self.f_type = f_type
    self.data = data
    self.broadcast_domain = broadcast_domain

  def __repr__(self):
    return "Ethernet Frame: Source: {} Dest: {} Type: {} Data: {} Broadcast Domain {}".format(
      self.source_mac_addr,
      self.dest_mac_addr,
      self.f_type,
      self.data,
      self.broadcast_domain
    )
