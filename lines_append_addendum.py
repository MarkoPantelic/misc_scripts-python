#!/usr/bin/python3

# ========================================================== #
#              lines_append_addendum.py
#  Append addendum string to the end of every line in a file
# ========================================================== #


in_filename = "in_filename.txt"
out_filename = "out_filename.txt"
addendum = "\",\n"


with open(in_filename, 'r') as inf:
	with open(out_filename, 'w') as outf:
		l = inf.readline()
		while l:
			outf.write(l.strip("\n") + addendum)
			l = inf.readline()
	
