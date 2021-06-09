#!/usr/bin/env python
"""reducer.py"""

import sys
from collections import Counter
import ast


all_coauths = {}
author = None
old_auth = None


for line in sys.stdin:
	line = line.strip()

	author, coauths = line.split('\t')
	coauths = ast.literal_eval(coauths)

	if old_auth == author:
		new_coauths = Counter(coauths)
		old_coauths = Counter(all_coauths)
		all_coauths = dict(new_coauths + old_coauths)
    	else:
        	if old_auth:
	    		print '%s\t%s' % (old_auth, all_coauths)
		all_coauths = coauths
		old_auth = author

if old_auth == author:
	print '%s\t%s' % (old_auth, all_coauths)


