import ns

node1 = ns.ethernet.Node(ns.mac_address_factory())
node2 = ns.ethernet.Node(ns.mac_address_factory())
switch = ns.ethernet.Switch(ns.mac_address_factory(), 4)
ns.ethernet.connect(switch, node1)
ns.ethernet.connect(switch, node2)
print(node1)
print(node2)
print(switch)
node1.send('hello from node 1', node2.mac_addr)
