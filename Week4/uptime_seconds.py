#!/usr/bin/env python

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'


# Putting all values into single list

uptimes = [uptime1,uptime2,uptime3,uptime4]

# Dictionary to store final values

d = {}
# List to store all seconds values for each element

seconds = []
# Variable to store seconds 

s1sec = 0


try:
	for times in uptimes:
		s1sec = 0
		# We are splitting each line into elements separated by space, we will need values from 4th element , 
		# 1st - hostname , 2 - uptime, 3 - is , 4th element till the end is our actual uptime value
		# Temporary list store in s1 variable will have numeric values along with words years,weeks,days,hours,minutes stored in it as separate  element

		s1 = times.split()[3:]
		# Going over the list 
		for line in range(0,len(s1)):
			# If we found word year or years we will multiply previous element which will be number by amount of seconds in year
			# 1 year has 365 days * 24 hours per day * 3600 seconds per day = 31,536,000 seconds
			if (s1[line] == "years,") or (s1[line] == "year,"):
				s1sec = s1sec + int(s1[line-1]) * 31536000
			# Similarly we will search for week or weeks keyword. If it is the list, then we will multiply previous element by amount of seconds in week
			# 1 week has 7 days * 24 hours per day * 3600 seconds per day = 604,800 seconds 
			if (s1[line] == "weeks,") or (s1[line] == "week,"):
				s1sec = s1sec + int(s1[line-1]) * 604800
			# The same is true for days, where each day is equal to 86400 seconds
			if (s1[line] == "days,") or (s1[line] == "day,"):
				s1sec = s1sec + int(s1[line-1]) * 86400
			# The same is true for hours, where each hour is equal to 3600 seconds
			if (s1[line] == "hours,") or (s1[line] == "hour,"):
				s1sec = s1sec + int(s1[line-1]) * 3600
			# Finally minutes, which is 60 seconds
			if (s1[line] == "minutes") or (s1[line] == "minute"):
				s1sec = s1sec + int(s1[line-1]) * 60
		# Each uptime per device value in seconds will be stored in the list called seconds.
		seconds.append(s1sec)

# Once above loop is finished, we should have four elements in seconds list. now we will need to extract keys in form of hostnames and...
# assign it to the dictionary

# Hostname will be very first element after we split each line separating by space. 
# We are going to assign to our dictionary key equal to the previous found values of seconds stored in the list

	for lines in range(0,len(uptimes)):
		d[uptimes[lines].split()[0]] = seconds[lines]
except ValueError:
	print "There has been error in conversion"


print d
