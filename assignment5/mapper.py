#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) > 1 :
		file_url_name = str(data[6]).strip()
		print "{0}".format(file_url_name)
