class TinyIntError(Exception):
    def __init__(self):
        self.message = 'El numero no cuenta como un Int'

    def __str__(self):
        return self.message