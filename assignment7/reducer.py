#!/usr/bin/python

import sys
req=dict()
for line in sys.stdin:
	line=line.split("\n")[0]
	req[line]=int(req.get(line,0))+1
for key in req.viewkeys():
	print "{0} {1}".format(key,req.get(key))
