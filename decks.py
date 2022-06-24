import card
import random
class Deck:
  def genDeck(self):
    self.colors = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    self.deck = []
    self.deck = [card.Card(value, color) for value in range(1,14) for color in self.colors]
    
  def shuffle(self):
    random.shuffle(self.deck)
  
  def getAndRemove(self):
    card = self.deck[0]
    del self.deck[0]
    return card
  