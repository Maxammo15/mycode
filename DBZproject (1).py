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
            self.health = 250
            self.strength = randint(30,40)
            self.ki = 120
        elif self.type == 2:
            self.health = 300
            self.strength = randint(40,50)
            self.ki = 150
        elif self.type == 3:
            self.health = 200
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
            self.enemy_type = 7
        if self.enemy_name == "Gohan":
            self.enemy_type = 8
        if self.enemy_name == "Hercule":
            self.enemy_type = 9

        if self.enemy_type == 4:
            self.enemy_health = 150
            self.enemy_strength = randint(20,30)
            self.enemy_ki = 100
        elif self.enemy_type == 5:
            self.enemy_health = 220
            self.enemy_strength = randint(30,50)
            self.enemy_ki = 150
        elif self.enemy_type == 6:
            self.enemy_health = 210
            self.enemy_strength = randint(30,40)
            self.enemy_ki = 130
        elif self.enemy_type == 7:
            self.enemy_health = 220
            self.enemy_strength = randint(30,50)
            self.enemy_ki = 140
        elif self.enemy_type == 8:
            self.enemy_health = 200
            self.enemy_strength = randint(30,40)
            self.enemy_ki = 150
        elif self.enemy_type == 9:
            self.enemy_health = 120
            self.enemy_strength = randint(10,20)
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

    def firstAttack():
        print("The stronger fighter atacks first\n")
        if player1.my_stats[2] > player1.enemy_stats[2]:
            player1.my_turn = True
        elif player1.enemy_stats[2] >= player1.my_stats[2]:
            player1.my_turn = False
        return player1.my_turn

    def attackThem():
        print(player1.my_stats[0] + " attacks!")
        attack_damage = int(player1.strength)
        player1.enemy_health -= attack_damage
        player1.my_turn = True
        if player1.enemy_health <= 0:
            print(player1.enemy_stats[0] + " HAS DIED")
            print(player1.my_stats[0] + " WINS!!!")
        else:
            print("Attack hits for " + str(attack_damage) + " damage.")
            print(player1.enemy_stats[0] + " has " + str(player1.enemy_health) + " health left.\n")

    def attackMe():
        print(player1.enemy_stats[0] + " attacks!")
        attack_damage = int(player1.enemy_strength)
        player1.health -= attack_damage
        player1.my_turn = False
        if player1.health <= 0:
            print(player1.my_stats[0] + " HAS DOED")
            print(player1.enemy_stats[0] + " WINS!!!")
        else:
            print("Attack hits for " + str(attack_damage) + " damage.")
            print(player1.my_stats[0] + " has " + str(player1.health) + " health left.\n")

    def duringFight():
        while player1.health > 0 and player1.enemy_health > 0:
            if player1.my_turn == True:
                attackThem()

            
            elif player1.my_turn == False:
             attackMe()
            
        
  
player1 = Fighter()
player1.createChar()
player1.firstAttack()
player1.duringFight()