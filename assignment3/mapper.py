#!/usr/bin/python
from urlparse import urlparse
import sys
for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) > 1 :
		pathname = data[6]
		pathname=urlparse(pathname).netloc+urlparse(pathname).path
		filename=urlparse(pathname).path
		print "{0}\t{1}".format(pathname,filename)
