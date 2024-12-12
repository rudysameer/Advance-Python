class Father:
    def __init__(self):
        print("2 hands and 2 feet")

    def skills(self):
        print("Driving, Communication, Kindness, calmness")

class Mother:
    def __init__(self):
        print("thick Black hair")

    def skills(self):
        print("Beautiful, Smartness, Cunning")

class Child(Father,Mother):
    def skills(self):
        Mother.__init__(self)
        Mother.skills(self)
        Father.skills(self)
        
        print("Studying, learning, Playing")            

c = Child()
c.skills()        