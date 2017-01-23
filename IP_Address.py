#!/usr/bin/env python
# Print IP Address
ip_addr = raw_input("Please enter IP address:")
ip_addr = ip_addr.split(".")
print ip_addr
print "{:<12} {:<12} {:<12} {:<12}".format(*ip_addr)
