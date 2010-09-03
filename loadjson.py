# very crude script doesn't even catch exceptions
# basically I just ran these commands one by one inside ipython

import couchdb

json1k = open('ol1k.json').readlines()
json100k = open('ol100k.json').readlines()

server = couchdb.Server('http://localhost:5984/')
db1k = server.create('ol1k')
db100k = server.create('ol100k')

docs1k = [ db1k.save(x) for x in json1k ]
docs100k = [ db100k.save(x) for x in json100k ]

