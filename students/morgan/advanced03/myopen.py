


class myopoen:
    def __init__(self, path, flags='r'):
        self.path = path
        self.flags = flags

    def __enter__(self):
        self.f = open(self.path, self.flags)
        return self.f




    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        return False