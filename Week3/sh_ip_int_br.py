#!/usr/bin/env python


show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''
b= []
new_list = []
# Splitting given output into new lines
a = show_ip_int_brief.split("\n")
# Going over each line starting with second element, since first one will be empty line (new line)
for k in range(1,len(a)):
# Appending to new list elements of previous list by splitting again lines
	b.append(a[k].split())
# Here were are going to remove columns 2 and 3 starting with 0
for m in range(0,len(b)-1):
	del b[m][3]
	del b[m][2]
# Sequence is important, if we delete column 2 first, then our column 3 will shift to its place, so we will need to delete it again
# alternative way of doing it is like this
  # del b[m][2]
  # del b[m][2]

# Finally we are going over the list where our columns 2 and 3 now should contain status and protocol. 
# If they both up we are going to assign it to a new list
for z in range(0,len(b)-1):
	if (b[z][2] == "up") and (b[z][3] == "up"):
		new_list.append(b[z])
for z in new_list:
	print z