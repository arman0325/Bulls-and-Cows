import random

class BullsAndCows:
    def __init__(self):
        self.choose=[1,2,3,4,5,6,7,8,9,0]
        self.ansList=[]
        self.endGame=False
        self.mode="N"

    def reset(self,cl):
        self.choose=[1,2,3,4,5,6,7,8,9,0]
        self.ansList=[]
        self.endGame=False
        cl.createAns()

    def createAns(self):
        ans = []
        numList = self.choose
        for x in range(4):
            num = random.choice(numList)
            ans.append(num)
            numList.remove(num)
        self.ansList = ans

    def checkAns(self, numList):
        a,b = 0,0
        Elist=""
        for x in range(4):
            if int(numList[x]) in self.ansList and int(numList[x]) == self.ansList[x]:
                a+=1
                Elist+="O"
            elif int(numList[x]) in self.ansList:
                b+=1
                Elist+="X"
            else:
                Elist+="-"
        if a == 4:
            print("You are win!")
            self.endGame = True
        else:
            if self.mode=="E":
                print(Elist)
            else:
                print("{}A{}B".format(a,b))
        

    def changeMode(self,m):
        self.mode=m

    def enterAns(self,cl):
        time = 8
        while True:
            if time == 0:
                print("You are lose~~")
                break
            if self.endGame:
                print("The game is completed. Please to restart!")
                break
            else:
                num = input("Enter the 4 digit number: ")
                cl.checkAns(num)
                time-=1

    def actionList(self):
        print("Action List:")
        print("s: Start the game")
        print("r: Reset the game")
        print("m: Select the mode level")
        print("e: End Game")
        print("h: help")
        

    def run(self):
        p = mind()
        p.createAns()
        p.actionList()
        while True:
            action = input("Enter the action: ")

            if action == "s":
                p.enterAns(p)
            elif action == "e":
                print("Thank you for your play!\nbye~")
                break
            elif action == "r":
                p.reset(p)
                print("Game is reseted")
            elif action == "c":
                print(p.ansList)
            elif action == "m":
                mode = input("Enter the mode (E/N): ")
                p.changeMode(mode)
            elif action == "h":
                p.actionList()

if __name__ == "__main__":
    a = BullsAndCows()
    a.run()
