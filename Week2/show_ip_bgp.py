#!/usr/bin/env python

entry1 = "*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233     0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233     0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"

# Variable to hold column1 title
column1 = "ip_prefix"
# Variable to hold column2 title

column2 = "as_path"

# printing using formatting 
print "%-20s %-20s" % (column1,column2)

# creating list of entries

entry = [entry1,entry2,entry3,entry4]

# going over the list 
for each in entry:
	# assigning second element of the list to ip_prefix. First element would be "*"
	ip_prefix = each.split()[1]
	# assigning fouth element of the list to as_path all the way down ,exluding last element which is "i"
	as_path = each.split()[4:-1]
	print "%-20s %-20s" % (ip_prefix,as_path)

