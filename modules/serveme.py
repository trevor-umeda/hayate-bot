#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys
import json
import urllib
from datetime import datetime, timedelta


url = 'http://gdata.youtube.com/feeds/api/videos?orderBy=relevance&max-results=1&alt=json&q=%s'


def SearchAndPrint(search_terms):
  request = urllib.urlopen(url % search_terms)
  payload = json.loads(request.read())  
  feed = payload['feed']  
  entries = feed['entry'][0]  
  links = entries['link']
  
  finalLink = links[0]['href']
  print(finalLink)

index = len(sys.argv)
query = ""
for x in range(1, index):
    query += sys.argv[x] + " "

searchQuery = query
SearchAndPrint(searchQuery)


