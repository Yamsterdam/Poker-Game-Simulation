import player
import decks
import engine
import random
class Sim(object):
    river = []
    players = []
    e = engine.Engine()
    
    def __init__(self, p, c):
        self.totalPlayers = p
        self.stratCoefficient = c
        self.deck = decks.Deck();
    def simGame(self):
        self.deck.genDeck();
        self.deck.shuffle();
        self.genPlayers()
        self.genRiver()
    
    def resetGame(self):
        self.players = []
        self.river = []
    
    def genPlayers(self):
        for i in range(self.totalPlayers-1):
            self.players.append(player.Player(False, random.random(), self.deck.getAndRemove(), self.deck.getAndRemove(), i+1))
        self.players.append(player.Player(True, self.stratCoefficient, self.deck.getAndRemove(), self.deck.getAndRemove(), len(self.players)+1))

    def genRiver(self):
        for i in range(5):
            self.river.append(self.deck.getAndRemove())

    def getWinner(self):
        played = []

        for i in self.players:
            if(i.folded != True):
                played.append(i)
                
        for i in played:
            i.setValue(self.e.getValue(i.cardOne, i.cardTwo, self.river))

        if(len(played) != 0):
            winners = [played[0]]
            for i in played:
                if i.value > winners[0].value:
                    winners[0] = i

                else: 
                    if i.value == winners[0].value and i.num != winners[0].num:
                        winners.append(i)
            
            return winners
        return 0
    
    def getScores(self):
        played = []
        scores = []
        for i in self.players:
            if(i.folded != True):
                played.append(i)
                
        for i in played:
            scores.append(i.value)
        
        return scores

    def getFolded(self):
      for i in self.players:
        if i.main == True:
          if i.folded == True:
            return True
          else:
            return False
            