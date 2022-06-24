class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def stringCard(self):
      return str(self.value) + " of " + self.color