#!/usr/bin/python

import sys
yr=dict()
for line in sys.stdin:
	if "2009" in str(line):
		yr[2009]=int(yr.get(2009,0))+1
	if "2010" in str(line):
		yr[2010]=int(yr.get(2010,0))+1
	if "2011" in str(line):
		yr[2011]=int(yr.get(2011,0))+1
print "2009 {0}".format(yr.get(2009))
print "2010 {0}".format(yr.get(2010))
print "2011 {0}".format(yr.get(2011))
print "{0} year had maximum number of hits.".format(str(max(yr,key=yr.get)))
