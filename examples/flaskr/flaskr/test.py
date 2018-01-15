"""
test stub
"""

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
r2 = r.get('aaa')
r3 = r.get('foo')