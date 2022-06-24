from numpy import equal


class Engine(object):

  def getValue(self, cardOne, cardTwo, river):
    hand = []
    for c in river:
      hand.append(c)
    hand.append(cardOne)
    hand.append(cardTwo)
    if (self.check_royal_flush(hand) != False):
        return 1000000000000
    
    if (self.check_straight_flush(hand) != False):
        return self.check_straight_flush(hand) + 10000000
    
    if (self.check_four_of_a_kind(hand) != False):
        return self.check_four_of_a_kind(hand) + 1000000
    
    if (self.check_full_house(hand) != False):
        return self.check_full_house(hand) + 100000
    
    if (self.check_flush(hand) != False):
        return self.check_flush(hand) + 10000
    
    if (self.check_straight(hand) != False):
        return self.check_straight(hand) + 1000
    
    if (self.check_three_of_a_kind(hand) != False):
        return self.check_three_of_a_kind(hand) + 100
    
    if (self.check_two_pair(hand) != False):
        return self.check_two_pair(hand) + 10
    
    if (self.check_pair(hand) != False):
        return self.check_pair(hand)
    
    if (self.high_card(hand) != False):
        return self.high_card(hand)
    
    return 0

  
  def check_royal_flush(self, hand):
    count = 0
    flush = []
    for i in range(len(hand)-1):
        if hand[i].color == hand[i+1].color:
            count += 1
            flush.append(hand[i].value)
        else:
            count = 1
        if count == 5:
            return self.check_royal(flush)
    return False

  def check_royal(self, hand):
      if 14 in hand and 13 in hand and 12 in hand and 11 in hand and 10 in hand:
          return True
      return False

  def check_straight_flush(self, hand):
    if self.check_flush(hand) != False and self.check_straight(hand) != False:
        return self.check_straight(hand)
    return False

  def check_four_of_a_kind(self, hand):
    count = 0
    cardV = -1
    for i in range(len(hand)-1):
        if hand[i].value == hand[i+1].value:
            count += 1
            cardV = hand[i].value
        else:
            count = 1
        if count == 4:
            return cardV * 4
    return False

  def check_full_house(self, hand):
    if self.check_three_of_a_kind(hand) != False and self.check_pair(hand) != False:
        return self.check_three_of_a_kind(hand)
    return False

  def check_flush(self, hand):
    count = 0
    flush = []
    for i in range(len(hand)-1):
        if hand[i].color == hand[i+1].color:
            count += 1
            flush.append(hand[i])
        else:
            count = 1
        if count == 5:
            return self.high_card(flush)
    return False

  def check_straight(self, hand):
    count = 0
    high = -1
    hand.sort(key=lambda x: x.value, reverse=False)
    for i in range(len(hand)-1):
        if(hand[i].value + 1 == hand[i+1].value):
            count += 1
            high = hand[i+1].value
        else:
            count = 0
        if count == 5:
            return high
    return False

  def check_three_of_a_kind(self, hand):
    count = 0
    cardV = -1
    for i in range(len(hand)-1):
        if hand[i].value == hand[i+1].value:
            count += 1
            cardV = hand[i].value
        else:
            count = 1
        if count == 3:
            return cardV * 3
    return False

  def check_two_pair(self, hand):
    count = 0
    pairs = []
    for i in range(0, len(hand)):    
        for j in range(i+1, len(hand)):    
            if(hand[i].value == hand[j].value):    
                count += 1
                pairs.append(hand[i])
    if count == 2:
        high = 0
        for c in pairs:
            high = max(c.value, high)
        secondHigh = 0
        for c in pairs:
            if c.value != high and c.value > secondHigh:
                secondHigh = c.value
        return (high*2) + (secondHigh*2)
    return False


  def check_pair(self, hand):
    count = 0
    pairs = []
    for i in range(0, len(hand)):    
        for j in range(i+1, len(hand)):    
            if(hand[i].value == hand[j].value):    
                count += 1
                pairs.append(hand[i])
    if count == 1:
        high = 0
        for c in pairs:
            high = max(c.value, high)
        return high * 2
    return False

  def high_card(self, hand):
    high = 0;
    for c in hand:
      high = max(high, c.value)
    return high
