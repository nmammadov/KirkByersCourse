#!/usr/bin/env python

sh_ver = """
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102 """

# our dictionary to store key and values
d = {}
# temporary list to extract elements from the output.
a = []

# output will be stored in the list , each elements separated by new line 
output = sh_ver.split("\n")
for lines in output:
	if "Cisco IOS Software" in lines:
		# Adding line to the list. It will always contain one line and single element number [0]. 
		#We will clear the list for the next IF statement
		a.append(lines)
		# Extracting vendor "Cisco" by splitting line separated by comma, which will give us "Cisco IOS Software"
		# Further we will split it again but separating by space and access first element which will be "Cisco".
		# We will store it as a key 'vendor' in our dictionary
		d['vendor'] = a[0].split(',')[0].split(' ')[0]
		# Similarly we will do the same procedure for our main line and access third element which will be "Version 15.0(1)M4"
		# From there we will need to get rid of word "Version" , so first we will strip all spaces to the left and split this element by space
		# We will have two elements "Version" and "15.0(1)M4". So our IOS_versoin will be assigned to second element
		d['os_version'] = a[0].split(',')[2].lstrip(' ').split(' ')[1]
		# We will clear our temporary list for the next task
		a = []
	if "bytes of memory" in lines:
		a.append(lines)
		# Split the line by spaces and we will need second element, which will be  "881", i.e our model
		d['model'] = a[0].split(' ')[1]
		a = []
	if "Processor board ID" in lines:
		a.append(lines)
		# Split the line by spaces and we will need element number 4, which will be our serial number
		d['serial_number'] = a[0].split(' ')[3]
		a = []
	if "uptime is" in lines:
		a.append(lines)
		# This is a little bit tricky. We used two temporary variables b and c. 
		# b will store line split and 4th element till the end : 1st element is hostname, 2nd - uptime, 3rd - is. 
		# Starting with 4th element till the end is our uptime. But if we leave it this way, everything will be stored as individual 
		# element of list. That's why we use variable "c" to take all values of uptime and store is as a single element.
		# this is eventually will be assigned to our dictionary under "uptime" key
		b = a[0].split()[3:]
		c = " ".join(b)
		d['uptime'] = c
		a = []
print d
