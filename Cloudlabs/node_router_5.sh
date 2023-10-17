#!/bin/bash

# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Add routes
ip route add 192.168.2.0/24 via 192.168.2.6 
ip route add 192.168.3.0/24 via 192.168.5.2 

# Set up the default route
ip route add default via 192.168.2.3
