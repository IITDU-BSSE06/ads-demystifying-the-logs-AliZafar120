#!/usr/bin/python
from urlparse import urlparse
import sys

for line in sys.stdin:
	data = line.strip().split("GET ")
	if len(data) > 1 :
		file_url_name = data[1].split(" ")[0]
		file_url_name=urlparse(file_url_name).netloc+urlparse(file_url_name).path
		print "{0}".format(file_url_name)
