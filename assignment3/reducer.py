#!/usr/bin/python

import sys

hitcount=0
oldfile =None
maxhitfile=None
maxcount=0
maxhitfullpath=None
fullpath=None
for line in sys.stdin:
	fullpath=line.split("\t")[0]
	filename=line.split("\t")[1]
	if oldfile and oldfile != str(filename):		
		if maxcount<hitcount:
			maxcount=hitcount
			maxhitfile=oldfile
			maxhitfullpath=fullpath
		oldfile=filename
		hitcount=0
	oldfile=str(filename)
	hitcount=hitcount+1
if maxcount<hitcount:
	maxcount=hitcount
	maxhitfile=oldfile
	maxhitfullpath=fullpath				
print "{0} it hitted max times. And full path is {1}".format(maxhitfile,maxhitfullpath)
	
