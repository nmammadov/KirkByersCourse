#!/usr/bin/env python

import sys
ipvalid = False

# Checking if two arguments were passed, with 1st being script name itself, second one - ip address. 
#If none or more than two are passed, exiting the program

while ipvalid == False:
	ip = raw_input("Please enter ip address :")
	# Splitting ip addresses into octets separated by comma
	octets = ip.split(".")
	a = len(octets)
	o1 = int(octets[0])
	o2 = int(octets[1])
	o3 = int(octets[2])
	o4 = int(octets[3])
	if (a == 4) and (o1 != 127) and (1 <= o1 <= 223) and (0 <= o2 <= 255) and (0 <=o3 <= 255) and (0 <=o4 <= 255) and ((o1 != 169) or (o2 !=254)):
		print "IP address {} is valid".format(ip)
		ipvalid = True
	else:
		print "IP address {} is NOT VALID. Please try again".format(ip)		




