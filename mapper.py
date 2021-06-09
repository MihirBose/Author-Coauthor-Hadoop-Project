#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""mapper.py"""

import sys
import json
import re


for line in sys.stdin:
    line = line.strip()
    line = ''.join(c if ord(c) < 129 else '?' for c in line)
    data = json.loads(line)
    data_list = data['articles']
    for info in data_list:
        stripe = {}
        list_of_authors = info['authors'].split(', ')
	for index, a in enumerate(list_of_authors):
            #list_of_authors[index] = a.encode('utf-8', 'ignore').decode('utf-8')
	    list_of_authors[index] = a.encode('ascii', 'ignore').decode('ascii').encode('utf-8')
        main_author = list_of_authors[0] # Get the first author
        list_of_authors = list_of_authors[1:] # Get only the co-authors
        for co_auth in list_of_authors:
            stripe[co_auth] = 1
        print '%s\t%s' % (main_author, stripe)