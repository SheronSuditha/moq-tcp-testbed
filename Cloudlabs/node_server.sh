#!/bin/bash

# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Set up the default route
ip route add default via 192.168.8.2
