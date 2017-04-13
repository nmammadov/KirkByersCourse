#!/usr/bin/env python

import fileinput

for line in fileinput.input():
    print line.strip('\n').split(".")

# Here we are using strip method to remove new line and then splitting string into list using "." as delimeter 