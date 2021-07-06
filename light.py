class Light(object):
    """A Light Shines."""

    def __init__(self, lumens):
        self.lumens = lumens
        self.is_on = False

    def __repr__(self):
        return f'Light(lumens={self.lumens})'

    def shine(self):
        if self.is_on is False:
            return 0
        else:
            return self.lumens

    def power_on(self):
        self.is_on = True

    def power_off(self):
        self.is_on = False
