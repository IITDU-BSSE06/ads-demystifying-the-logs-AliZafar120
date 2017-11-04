#!/usr/bin/python

import sys
from urlparse import urlparse
for line in sys.stdin:
	data = line.strip().split("GET ")
	if len(data) > 1 :
		pathname = data[1].split(" ")[0]
		filename=urlparse(pathname).path
		print "{0}".format(filename)
