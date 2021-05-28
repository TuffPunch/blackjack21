import GameProcess 
from tkinter import *
import Player

def GUI(player,dealer):
    
  
    
    ##Widgets##
    mainscreen = Tk()
    mainscreen.geometry('720x480')
    mainscreen.title('BlackJack21 By Noobcoder810')
    mainscreen.configure(bg='#007500')
    Hitbtn = Button(mainscreen,text="Hit",font=('Arial',30))
    Stickbtn = Button(mainscreen,text="Stick",font=('Arial',30))
   
    ps = StringVar()
    ps.set(player.score)
    ds = IntVar()
    ds.set(dealer.score)
    output = StringVar()
    output.set('Game Started!')
    PlayerScore = Label(mainscreen,textvariable=ps,font=('Arial',30),width=7,bg='#007500',fg='#ffffff')
    DealerScore = Label(mainscreen,textvariable=ds,font=('Arial',30),width=7,bg='#007500',fg='#ffffff')
    Playerlbl = Label(mainscreen,text='Player',font=('Arial',30),width=7,bg='#007500',fg='#ffffff')
    Dealerlbl = Label(mainscreen,text='Dealer',font=('Arial',30),width=7,bg='#007500',fg='#ffffff')
    OutputLbl = Label(mainscreen,textvariable=output,font=('Arial',30),width=20,bg='#007500',fg='#ffffff')
    
    
    
    ##Packing
    PlayerScore.place(x=50,y=60)
    Playerlbl.place(x=50,y=10)
    DealerScore.place(x=488,y=60)
    Dealerlbl.place(x=488,y=10)
    OutputLbl.place(x=115,y=240)
    Hitbtn.place(x=50,y=340)
    Stickbtn.place(x=488,y=340)
    
    ##Commands
    game = GameProcess.GameProcess(player,dealer,output,ps,ds,mainscreen)
    Hitbtn['command'] = lambda p=player,o=output,pso=ps,ms=mainscreen: game.hit(player=p,output=output,pso=pso,mainscreen=ms)
    Stickbtn['command'] = lambda p=player,d = dealer,dso=ds,o=output,pso=ps,mainscreen=mainscreen: game.stick(p,d,o,pso,dso,mainscreen)



    ##Launch    
    
    mainscreen.mainloop()
    
