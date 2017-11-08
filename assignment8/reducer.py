#!/usr/bin/python

import sys
files=dict()
for line in sys.stdin:
	files[line]=int(files.get(line,0))+1
maxhit=str(max(files,key=files.get))
print "{0} {1}".format(maxhit.split("\n")[0], files.get(maxhit))
