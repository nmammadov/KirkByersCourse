#!/usr/bin/env python

# Task 1
# Split given ipv6 address into 4 hex octets

address = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719"
addrsplit = address.split(':')
print ('Splitted IPv6 address is : ')
print (addrsplit)

# Task 2
# Assemble address back to original

addrjoined = ":".join(addrsplit)
print ('Joined IPv6 address is : ')
print (addrjoined)


