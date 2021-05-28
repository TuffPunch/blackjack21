import random
import Player
import time
class GameProcess:
    cards = [2,3,4,5,6,7,8,9,10,10,10,'A',2,3,4,5,6,7,8,9,10,10,10,'A',2,3,4,5,6,7,8,9,10,10,10,'A',2,3,4,5,6,7,8,9,10,10,10,'A']
    def hit(self,player,output,pso,mainscreen):
        
        c = self.cards[random.randint(0,len(self.cards)-1)]
        if c == 'A':
            if player.score + 10 > 21:
                player.score += 1
            else:
                player.score += 10
        else:
            player.score += c        

            if player.id == 'Player':
                pso.set(player.score)
                
            if player.score > 21:
                output.set(player.id+" lose!")
                mainscreen.after(1000,lambda : mainscreen.destroy())       
            self.cards.remove(c)
           

    def stick(self,player,dealer,output,pso,dso,mainscreen):
        while dealer.score < player.score and dealer.score < 21:
                self.hit(dealer,output,dso,mainscreen)
                dso.set(dealer.score)
        dso.set(dealer.score)    
        if dealer.score == player.score:
            output.set("It's a draw")
            player = Player.Player(1)
            dealer = Player.Player(2)
            GameProcess(player,dealer,output,pso,dso,mainscreen)
        elif dealer.score > 21:
            output.set("You win! Congratz!")
            mainscreen.after(1000,lambda : mainscreen.destroy())
        else:
            output.set("You lose!") 
            mainscreen.after(1000,lambda : mainscreen.destroy())

    

    def __init__(self,player,dealer,output,pso,dso,mainscreen):
        output.set('New Game!')
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        self.hit(player,output,pso,mainscreen)
        self.hit(player,output,pso,mainscreen)
        pso.set(player.score)
        self.hit(dealer,output,dso,mainscreen)
        dso.set(dealer.score)
        self.hit(dealer,output,dso,mainscreen)
        #self.roundv0(player,dealer)

   
               
            


    
