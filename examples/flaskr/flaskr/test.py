"""
test stub
"""

import MySQLdb
db=MySQLdb.connect(user="root",db="entries")
# r = redis.StrictRedis(host='localhost', port=6379, db=0)
# r.set('foo', 'bar')
# r2 = r.get('aaa')
# r3 = r.get('foo')

cursor = db.cursor()
print(cursor.execute('SELECT * FROM entries;'))