import tkinter as tk
from tkinter import ttk
import player
import decks
import engine
import sim

root = tk.Tk()
root.geometry('500x300')
root.resizable(False, False)
root.title('Poker Sim')

playerGame = tk.StringVar()
gameNum = tk.StringVar()
strat = tk.StringVar()

e = engine.Engine()

def startGame():
  s = sim.Sim(int(playerGame.get()), float(strat.get()))
  mainWins = 0
  losses = 0
  bindCount = 1
  for x in range(int(gameNum.get())):
      s.simGame()
      if(s.getWinner() == 0):
          print("Everyone Folded Game: " + str(x))
      else: 
          scores = s.getScores()
          won = False
          stringScore = ""
          for score in scores:
              stringScore = stringScore + str(score) + ", "
          for win in s.getWinner():
              if(win.num == int(playerGame.get())):
                  print("won game: " + str(x) + " Scores: " + stringScore)
                  mainWins += 1
                  won = True
          
          if won == False:
            folded = s.getFolded()
            if folded == False:
              print("lost game: " + str(x) + " Scores: " + stringScore)
              losses += 1
            else:
              if bindCount != int(playerGame.get()) and bindCount != int(playerGame.get())-1: 
                print("won game not bind: " + str(x) + " Scores: " + stringScore)
                mainWins += 1
                bindCount += 1
                won = True
              else:
                print("lost game bind: " + str(x) + " Scores: " + stringScore)
                losses += 1
                if bindCount >= int(playerGame.get())-1:
                  bindCount = 1
                else:
                  bindCount += 1
      s.resetGame()
  print("Games Won: " + str(mainWins))
  print("Games lost: " + str(losses))


player_lbl = tk.Label(root, text = 'Number of Players (min 2)', font=('calibre',10, 'bold'))
  
player_entry = tk.Entry(root,textvariable = playerGame, font=('calibre',10,'normal'))
  
num_lbl = tk.Label(root, text = 'Number of trials (min 1)', font = ('calibre',10,'bold'))
  
num_entry=tk.Entry(root, textvariable = gameNum, font = ('calibre',10,'normal'))

strat_lbl = tk.Label(root, text = 'Strat (0-1% of hands played)', font = ('calibre',10,'bold'))
  
strat_entry=tk.Entry(root, textvariable = strat, font = ('calibre',10,'normal'))
  
sub_btn=tk.Button(root,text = 'Play', command = startGame)
  
player_lbl.grid(row=0,column=0)
player_entry.grid(row=0,column=1)
num_lbl.grid(row=1,column=0)
num_entry.grid(row=1,column=1)
strat_lbl.grid(row=2,column=0)
strat_entry.grid(row=2,column=1)
sub_btn.grid(row=3,column=1)
root.mainloop()