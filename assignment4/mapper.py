#!/usr/bin/python

import sys
for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) > 1 :
		pathname = data[6]
		filename=pathname
		print "{0}".format(filename)
