"""
the account structure
"""


class Account:
    def __init__(self, username, password):
        self.u = username
        self.p = password

    def get_pass(self):
        return self.p