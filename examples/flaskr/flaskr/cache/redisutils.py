"""
operations on redis
"""

import redis

# r = redis.StrictRedis()
from entity.account import Account


class RedisUtils:
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    def init_users(self):
        #self.r.set('test', Account('test', 'test'))
        self.r.set('test', 'test')
        self.r.set('testuser1', 'test')
        self.r.set('testuser2', 'test')

    def get_user(self, username=''):
        self.r.set_response_callback('HGET', str)
        return str(self.r.get(username))

    def is_user_exist(self, username=''):
        return self.r.get(username) is not None
