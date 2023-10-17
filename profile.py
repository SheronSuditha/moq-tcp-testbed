# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node router-4
node_router_4 = request.RawPC('router-4')
node_router_4.hardware_type = 'c220g1'
node_router_4.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_router_4.sh'))
iface0 = node_router_4.addInterface('interface:t-router4', pg.IPv4Address('192.168.2.4', '255.255.255.0'))
iface1 = node_router_4.addInterface('interface:router4', pg.IPv4Address('192.168.2.5', '255.255.255.0'))

# Node router-3
node_router_3 = request.RawPC('router-3')
node_router_3.hardware_type = 'c220g1'
node_router_3.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_router_3.sh'))
iface2 = node_router_3.addInterface('interface:t-router3', pg.IPv4Address('192.168.2.2', '255.255.255.0'))
iface3 = node_router_3.addInterface('interface:router3', pg.IPv4Address('192.168.2.3', '255.255.255.0'))

# Node router-5
node_router_5 = request.RawPC('router-5')
node_router_5.hardware_type = 'c220g1'
node_router_5.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_router_5.sh'))
iface4 = node_router_5.addInterface('interface:t-router5', pg.IPv4Address('192.168.2.6', '255.255.255.0'))
iface5 = node_router_5.addInterface('interface:router5', pg.IPv4Address('192.168.2.7', '255.255.255.0'))

# Node router-2
node_router_2 = request.RawPC('router-2')
node_router_2.hardware_type = 'c220g1'
node_router_2.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_router_2.sh'))
iface6 = node_router_2.addInterface('interface:t-router2', pg.IPv4Address('192.168.3.2', '255.255.255.0'))
iface7 = node_router_2.addInterface('interface:a-router2', pg.IPv4Address('192.168.4.2', '255.255.255.0'))

# Node router-1
node_router_1 = request.RawPC('router-1')
node_router_1.hardware_type = 'c220g1'
node_router_1.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_router_1.sh'))
iface8 = node_router_1.addInterface('interface:a-router1', pg.IPv4Address('192.168.3.3', '255.255.255.0'))
iface9 = node_router_1.addInterface('interface:b-router1', pg.IPv4Address('192.168.4.3', '255.255.255.0'))

# Node client2
node_client2 = request.RawPC('client2')
node_client2.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_client2.sh'))
node_client2.hardware_type = 'c220g1'
iface10 = node_client2.addInterface('interface:client2', pg.IPv4Address('192.168.2.1', '255.255.255.0'))

# Node moqpub
node_moqpub = request.RawPC('moqpub')
node_moqpub.hardware_type = 'c220g1'
node_moqpub.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_moqpub.sh'))
iface11 = node_moqpub.addInterface('interface:moqpub', pg.IPv4Address('192.168.7.2', '255.255.255.0'))

# Node client1
node_client1 = request.RawPC('client1')
node_client1.hardware_type = 'c220g1'
node_client1.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_client1.sh'))
iface12 = node_client1.addInterface('interface:client1', pg.IPv4Address('192.168.2.9', '255.255.255.0'))

# Node client3
node_client3 = request.RawPC('client3')
node_client3.hardware_type = 'c220g1'
node_client3.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_client3.sh'))
iface13 = node_client3.addInterface('interface:client3', pg.IPv4Address('192.168.2.8', '255.255.255.0'))

# Node server
node_server = request.RawPC('server')
node_server.hardware_type = 'c220g1'
node_server.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_server.sh'))
iface14 = node_server.addInterface('interface:b-server', pg.IPv4Address('192.168.8.1', '255.255.255.0'))
iface15 = node_server.addInterface('interface:d-server', pg.IPv4Address('192.168.9.1', '255.255.255.0'))

# Node router-6
node_router_6 = request.RawPC('router-6')
node_router_6.hardware_type = 'c220g1'
node_router_6.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_router_6.sh'))
iface16 = node_router_6.addInterface('interface:c-router6', pg.IPv4Address('192.168.6.1', '255.255.255.0'))
iface17 = node_router_6.addInterface('interface:b-router6', pg.IPv4Address('192.168.5.1', '255.255.255.0'))

# Node tcphost
node_tcphost = request.RawPC('tcphost')
node_tcphost.hardware_type = 'c220g1'
node_tcphost.addService(pg.Execute('/bin/sh', '/usr/bin/sudo /bin/bash /local/repository/CloudLab/node_tcphost.sh'))
iface18 = node_tcphost.addInterface('interface:b-tcphost', pg.IPv4Address('192.168.7.1', '255.255.255.0'))

# Link link-4
link_4 = request.Link('link-4')
link_4.addInterface(iface0)
link_4.addInterface(iface2)
link_4.addInterface(iface4)
link_4.addInterface(iface6)

# Link link-5
link_5 = request.Link('link-5')
link_5.addInterface(iface7)
link_5.addInterface(iface8)

# Link link-2
link_2 = request.Link('link-2')
link_2.addInterface(iface10)
link_2.addInterface(iface1)

# Link link-3
link_3 = request.Link('link-3')
link_3.addInterface(iface13)
link_3.addInterface(iface5)

# Link link-1
link_1 = request.Link('link-1')
link_1.addInterface(iface12)
link_1.addInterface(iface3)

# Link link-6
link_6 = request.Link('link-6')
link_6.addInterface(iface14)
link_6.addInterface(iface9)
link_6.addInterface(iface17)

# Link link-8
link_8 = request.Link('link-8')
link_8.addInterface(iface11)
link_8.addInterface(iface15)

# Link link-7
link_7 = request.Link('link-7')
link_7.addInterface(iface18)
link_7.addInterface(iface16)

# Print the generated RSpec
pc.printRequestRSpec(request)
