class Player:
    id = ""
    score = 0
    def __init__ (self,id):
        self.id = id 

    def PrintScore(self):
        print("\n"+self.id+" Score: "+str(self.score))