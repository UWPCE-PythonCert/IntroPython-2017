""" 
handle authorized users for database modification
"""


class UserLogger():

    def __init__(self):
        self.users = []

    def record_user(self, func):
        def get_user(*args, **kwargs):
            if not self.users:
                self.users.append(input("Please enter user name:\n"))
            return func(*args, **kwargs)
        return get_user
