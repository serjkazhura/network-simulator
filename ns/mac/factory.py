def _mac_address_factory():
  _mac_address = 160 # arbitary number

  def new_mac_address():
    nonlocal _mac_address
    _mac_address += 1
    return '{:012X}'.format(_mac_address)
  
  return new_mac_address

mac_address_factory = _mac_address_factory()