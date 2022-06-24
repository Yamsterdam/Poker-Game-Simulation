class Player:


  
  hands =["AA","KK","QQ","AKs","JJ","AQs","KQs","AJs","KJs","TT","AKo","ATs","QJs","KTs","QTs","JTs","99","AQo","A9s","KQo","88","K9s","T9s","A8s","Q9s","J9s","AJo","A5s","77","A7s","KJo","A4s","A3s","A6s","QJo","66","K8s","T8s","A2s","98s","J8s","ATo","Q8s","K7s","KTo","55","JTo","87s","QTo","44","33","22","K6s","97s","K5s","76s","T7s","K4s","K3s","K2s","Q7s","86s","65s","J7s","54s","Q6s","75s","96s","Q5s","64s","Q4s","Q3s","T9o","T6s","Q2s","A9o","53s","85s","J6s","J9o","K9o","J5s","Q9o","43s","74s","J4s","J3s","95s","J2s","63s","A8o","52s","T5s","84s","T4s","T3s","42s","T2s","98o","T8o","A5o","A7o","73s","A4o","32s","94s","93s","J8o","A3o","62s","92s","K8o","A6o","87o","Q8o","83s","A2o","82s","97o","72s","76o","K7o","65o","T7o","K6o","86o","54o","K5o","J7o","75o","Q7o","K4o","K3o","96o","K2o","64o","Q6o","53o","85o","T6o","Q5o","43o","Q4o","Q3o","74o","Q2o","J6o","63o","J5o","95o","52o","J4o","J3o","42o","J2o","84o","T5o","T4o","32o","T3o","73o","T2o","62o","94o","93o","92o","83o","82o","72o"]

  values = ["place", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


  
  def __init__(self, main, strat, cardOne, cardTwo, num):
    self.strat = strat
    self.main = main
    self.cardOne = cardOne
    self.cardTwo = cardTwo
    self.num = num
    amount = int(len(self.hands) * self.strat)
    self.playable = self.hands[:amount]
    pair = (cardOne.value == cardTwo.value)
    suited = (cardOne.color == cardTwo.color)
    if suited:
      suited = "s"
    else:
      suited = "o"

    firstCard = max(cardOne.value, cardTwo.value)
    secondCard = min(cardOne.value, cardTwo.value)
    formattedCard = ''
    if pair:
      formattedCard = self.values[firstCard] + self.values[secondCard]
    else:
      formattedCard = self.values[firstCard] + self.values[secondCard] + suited
  
    if formattedCard not in self.playable:
      self.folded = True
    else:
      self.folded = False

  def getCards(self):
    return self.cardOne.stringCard() + "\n" + self.cardTwo.stringCard()

  def setValue(self, value):
    self.value = value

