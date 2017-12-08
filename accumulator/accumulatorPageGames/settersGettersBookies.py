class SettersGettersBookies:
    # def __init__(self, bookie_name=''):
    #     self.bookies_name = bookie_name
    #
    def __init__(self, bookie_name=None):
        self.bookies_name = bookie_name

    def get(self):
        name = self.bookies_name
        return name

    def set(self, bookie_name):
        self.bookies_name = bookie_name
