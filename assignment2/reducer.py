#!/usr/bin/python

import sys

countTotal = 0
oldurl = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	url,hit	=	data
	if "/assets/js/the-associates.js" == str(url) :
		oldurl = url
		countTotal += int(hit)
print countTotal

