#!/usr/bin/python

import sys

for line in sys.stdin:
	data=line.strip().split(" ");
	if(len(data)>1):
		url_name=data[0]
		print url_name

