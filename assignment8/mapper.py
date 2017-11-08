#!/usr/bin/python

import sys
from urlparse import urlparse
for line in sys.stdin:
	data=line.split(" ")
	if(len(data)>6):
		filepath=urlparse(str(data[6])).path
		print filepath
