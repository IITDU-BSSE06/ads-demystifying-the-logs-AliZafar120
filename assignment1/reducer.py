#!/usr/bin/python

import sys

countTotal=0

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 1 :
		continue
	
	url_address= str(data[0])
	if "10.99.99.186" == url_address:
		countTotal+=1


print countTotal
