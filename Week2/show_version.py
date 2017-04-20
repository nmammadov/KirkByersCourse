#!/usr/bin/env python

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

# we are going to split output to elements that are separated by comma
output = cisco_ios.split(",")
# Now we have 4 elements and our Version is element number 2
# We are going to assign IOS version to element number 2 which will be equal to "Version 15.0(1)M4"
# Since we don't need word "Version" we can further split output into elements separated by space
# It will give us two elements: Version and 15.0(1)M4, so we are going to assign to our final variable second element
ios_version = output[2].split()[1]
print "IOS running is :" ,ios_version