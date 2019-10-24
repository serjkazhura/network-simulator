import ns

node1 = ns.ethernet.Node(ns.mac_address_factory())
node2 = ns.ethernet.Node(ns.mac_address_factory())
ns.ethernet.connect(node1, node2)
print(node1)
print(node2)
