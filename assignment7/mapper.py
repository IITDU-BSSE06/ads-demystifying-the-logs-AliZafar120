#!/usr/bin/python

import sys

for line in sys.stdin:
	data=line.split(" ")
	if(len(data)>=5):
		reqs=data[5].split("\"")
		if len(reqs)>1:
			print reqs[1]
