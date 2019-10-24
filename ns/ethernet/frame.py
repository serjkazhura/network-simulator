class EthernetFrame:
  def __init__(self, source_mac_addr, dest_mac_addr, f_type, data):
    self.source_mac_addr = source_mac_addr
    self.dest_mac_addr = dest_mac_addr
    self.f_type = f_type
    self.data = data

  
