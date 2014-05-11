#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys
import json
import urllib2
from datetime import datetime, timedelta


url = "http://linkcafe.herokuapp.com/link/createLink"

def SearchAndPrint(link,name):
  data = {
        'link': link,"user":name
  }
  req = urllib2.Request(url)
  req.add_header('Content-Type', 'application/json')
  response = urllib2.urlopen(req, json.dumps(data))      

index = len(sys.argv)
name = ""

for x in range(2, index):
    name += sys.argv[x] + " "

SearchAndPrint(sys.argv[1],name)

