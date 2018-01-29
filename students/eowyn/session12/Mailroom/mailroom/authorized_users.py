""" 
handle authorized users for database modification
"""
USERS = []

def record_user(func):
    print("inside decorator")
    def get_user(self, *args, **kwargs):
        if not USERS:
            USERS.append(input("Please enter user name:\n"))
        return func(self, *args, **kwargs)
    return get_user

