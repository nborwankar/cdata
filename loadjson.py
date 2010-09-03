#! /usr/bin/env python

""" Script to load json
 crude  - doesn't catch exceptions
 basically I just ran these commands one by one inside ipython
 and later created this script from them
"""

import couchdb
import simplejson

str1k = open('ol1k.json').read()
str100k = open('ol100k.json').read()

json1k = simplejson.loads(str1k)
json100k = simplejson.loads(str100k)

server = couchdb.Server('http://localhost:5984/')
db1k = server.create('ol1k')
db100k = server.create('ol100k')

docs1k = [ db1k.save(x) for x in json1k ]
docs100k = [ db100k.save(x) for x in json100k ]

