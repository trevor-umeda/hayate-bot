#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys
import json
import urllib
from datetime import datetime, timedelta


url = 'http://nagi.herokuapp.com/answer/answerQuestion?question=%s'


def SearchAndPrint(search_terms):
  request = urllib.urlopen(url % search_terms)
  payload = request.read()  
  print(payload)

index = len(sys.argv)
query = "what "
for x in range(1, index):
    query += sys.argv[x] + " "

searchQuery = query
SearchAndPrint(searchQuery)

