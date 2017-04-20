#!/usr/bin/env python

ip = raw_input("Please enter ip address = ")
network = ip.split(".")[0:3]
print len(network)
network = ".".join(network)
octets = ip.split(".")[0:3]
octets.append('0')
first_octet_bin = bin(int(octets[0]))
first_octet_hex = hex(int(octets[0]))
column1 = 'NETWORK_NUMBER'
column2 = "FIRST_OCTET_BINARY"
column3 = "FIRST_OCTET_HEX"

print "%-20s %-20s %-20s" % (column1,column2,column3)
print "%-20s %-20s %-20s" % (network,first_octet_bin,first_octet_hex)

