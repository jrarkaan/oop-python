class Hero:
    # class variable/ static variable
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
    
    # method without argument
    def siapa(self):
        print("namaku adalah %s"%(self.name))
    
    # method is return value
    def healthUp(self, up):
        self.health += up
    
    def getHealth(self):
        return self.health
        
hero1 = Hero("sniper", 100, 10, 5)
hero2 = Hero("mariana", 80, 3, 2)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())

# print(hero1.__dict__)
# print(hero2.__dict__)