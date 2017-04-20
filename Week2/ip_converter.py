#!/usr/bin/env python

ip = raw_input("Please enter ip address = ")
octets = ip.split(".")
first_octet_bin = bin(int(octets[0]))
second_octet_bin = bin(int(octets[1]))
third_octet_bin = bin(int(octets[2]))
fourth_octet_bin = bin(int(octets[3]))

column1 = 'first_octet'
column2 = "second_octet"
column3 = "third_octet"
column4 = "fourth_octet"

print "%-20s %-20s %-20s %-20s" % (column1,column2,column3,column4)
print "%-20s %-20s %-20s %-20s" % (first_octet_bin,second_octet_bin,third_octet_bin,fourth_octet_bin)

