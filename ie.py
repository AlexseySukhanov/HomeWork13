class IE(Exception):
    def __init__(self, exept, mesg):
        self.exept = exept
        self.mesg = mesg
