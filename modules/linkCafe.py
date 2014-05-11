#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys
import json
import urllib2
from datetime import datetime, timedelta


url = "http://localhost:8080/linkCafe/link/createLink"

def SearchAndPrint(link,name):
  data = {
        'link': link,"user":name
  }
  req = urllib2.Request(url)
  req.add_header('Content-Type', 'application/json')
  response = urllib2.urlopen(req, json.dumps(data))      

index = len(sys.argv)
name = ""

SearchAndPrint(sys.argv[1],sys.argv[2])

heroku config:set JAVA_OPTS='-Xmx384m -Xss512k -XX:+UseCompressedOops -javaagent:newrelic/newrelic.jar' NEW_RELIC_APP_NAME="linkcafe"
