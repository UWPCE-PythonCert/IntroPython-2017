'''Content Manager Exercise'''

class MyOpen:
    def __init__(self, name, flags):
        self.name = name
        self.flags = flags

    def __enter__(self):
        f = open(self.name, self.flags)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        return False

with MyOpen("myopen.py", 'r') as f:
    print(f)