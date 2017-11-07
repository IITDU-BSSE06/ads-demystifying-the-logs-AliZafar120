#!/usr/bin/python
from urlparse import urlparse
import sys
for line in sys.stdin:
	data = line.strip().split("GET ")
	if len(data) > 1 :
		pathname = data[1].split(" ")[0]
		pathname=urlparse(pathname).netloc+urlparse(pathname).path
		print "{0}".format(pathname)
