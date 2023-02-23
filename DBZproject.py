from random import randint
import time

class Fighter:
    
    def __init__(self):
        pass
    
    def getType(self):
        print("Characters include Fighter, Goku, and Frieza? ")
        self.type = int(input("Press 1 for Goku, 2 for Frieza, or 3 for Fighter. "))
    
    def callType(self):
        return self.my_type

    def getName(self):
            if self.type == 1:
                self.name = "Goku"
            if self.type == 2:
                self.name = "Frieza"
            if self.type == 3:
                self.name = "Fighter"

    def callName(self):
        return self.name
    
    def buildStats(self):
        if self.type == 1:
            self.health = 130
            self.strength = randint(30,40)
            self.ki = 120
        elif self.type == 2:
            self.health = 150
            self.strength = randint(40,50)
            self.ki = 150
        elif self.type == 3:
            self.health = 100
            self.strength = randint(20,30)
            self.ki = 100
    
    def myStats(self):
        self.my_stats = [self.name, self.type, self.strength, self.health, self.ki]
        print("Name, ID, STR, HP, KI")
        return self.my_stats
        
    def buildEnemy(self):
        possible_names = ["Krillin", "Cell", "Trunks", "Vegeta", "Gohan", "Hercule"]
        self.enemy_name = possible_names[randint(0,5)]
        if self.enemy_name == "Krillin":
            self.enemy_type = 4
        if self.enemy_name == "Cell":
            self.enemy_type = 5
        if self.enemy_name == "Trunks":
            self.enemy_type = 6
        if self.enemy_name == "Vegeta":
            self.enemy_type = 4
        if self.enemy_name == "Gohan":
            self.enemy_type = 5
        if self.enemy_name == "Hercule":
            self.enemy_type = 6

        if self.enemy_type == 4:
            self.enemy_health = 100
            self.enemy_strength = randint(70,90)
            self.enemy_ki = 100
        elif self.enemy_type == 5:
            self.enemy_health = 100
            self.enemy_strength = randint(50,70)
            self.enemy_ki = 150
        elif self.enemy_type == 6:
            self.enemy_health = 100
            self.enemy_strength = randint(50,70)
            self.enemy_ki = 130
        elif self.enemy_type == 7:
            self.enemy_health = 100
            self.enemy_strength = randint(50,70)
            self.enemy_ki = 140
        elif self.enemy_type == 8:
            self.enemy_health = 100
            self.enemy_strength = randint(50,70)
            self.enemy_ki = 150
        elif self.enemy_type == 9:
            self.enemy_health = 100
            self.enemy_strength = randint(50,70)
            self.enemy_ki = 50
        
    def getEnemy(self):
        self.enemy_stats = [self.enemy_name, self.enemy_type, self.enemy_strength, self.enemy_health, self.enemy_ki ]
        print("NAME, ID, STR, HP, KI")
        return self.enemy_stats

    def createChar(self):
        player1.getType()
        print("\n")
        player1.getName()
        print("\n")
        player1.buildStats()
        print(player1.myStats())
        print("VERSUS")
        player1.buildEnemy()
        print(player1.getEnemy())
        print("\n")
        
  
player1 = Fighter()
player1.createChar()