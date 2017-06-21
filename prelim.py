#!/usr/bin/python

import sys
import subprocess

if (len(sys.argv) != 2):
	print "ERROR: Invalid number of arguments, please execute the script again"
	exit()
	a	
print subprocess.check_output(['cd', sys.argv[1]])
print subprocess.check_output(['git','init'])
print subprocess.check_output(['echo', '1', '>>', '123454321.txt'])
print subprocess.check_output(['git','add', '.'])
print subprocess.check_output(['git','commit', '-m', '"iseegreen"'])
print subprocess.check_output(['git','push'])




#print "Repository target name is: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)