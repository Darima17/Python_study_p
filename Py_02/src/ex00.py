class Key:
    def __init__(self, passphrase):
        self.passphrase = passphrase

    def __len__(self):
        return 1337

    def __getitem__(self, index):
        return 3

    def __gt__(self, other):
        if other < 9000:
            return False
        return True

    def __eq__(self, other):
        return self.passphrase == other

    def __str__(self):
        return "GeneralTsoKeycard"
