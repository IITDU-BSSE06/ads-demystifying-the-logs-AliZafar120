#!/usr/bin/python

import sys

hitcount=0
oldfile =None
maxhitfile=None
maxcount=0
for filename in sys.stdin:
	if oldfile and oldfile != str(filename):		
		if maxcount<hitcount:
			maxcount=hitcount
			maxhitfile=oldfile
		oldfile=filename
		hitcount=0
	oldfile=str(filename)
	hitcount=hitcount+1
if maxcount<hitcount:
	maxcount=hitcount
	maxhitfile=oldfile			
print "{0}".format(maxcount)
