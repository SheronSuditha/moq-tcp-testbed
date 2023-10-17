#!/bin/bash

# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Add routes
ip route add 192.168.4.0/24 via 192.168.4.3 
ip route add 192.168.3.0/24 via 192.168.3.3 
