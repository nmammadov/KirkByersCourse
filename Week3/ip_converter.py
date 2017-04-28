#!/usr/bin/env python
import sys
octets_bin = []
new_octet_bin = []
column1 = 'IP Address'
column2 = "Binary"

# Checking if two arguments were passed, with 1st being script name itself, second one - ip address. 
#If none or more than two are passed, exiting the program

if len(sys.argv) == 2:
	#Assigning ip address to last argument 
	ip = sys.argv.pop()
	# Splitting ip addresses into octets separated by comma
	octets = ip.split(".")
	# Converting each octet into binary
	for addr in octets:
		octets_bin.append(bin(int(addr)))

	# Variable "a" is placeholder that wiil be assigned value after we will split each element separated by "0b". 
	# The result of the split will have two elements : [0] - will be empty space , [1] - will be anything after 0b, i.e that we need. 
	for addr in range(0,len(octets_bin)):
		a = octets_bin[addr].split("0b")[1]
	# Variable "b" will tell us how many "0" we will need to pad, which will be difference between 8 (8 bits) and our variable "a"
		b = 8 - len(a)
	# We will pad "0" to the list and append our value "a"
		new_octet_bin.append('0'*b + a)
	# Lastly we are going to create new variable and join all elements of our list by "."
		new_bin = ".".join(new_octet_bin)
	
	print "%-20s %-20s " % (column1,column2)
	print "%-20s %-20s " % (ip,new_bin)
		
else:
	print "Progam expects exactly 1 argument. None or more than 1 were given. Exiting"




