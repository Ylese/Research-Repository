# class Character:
#     name: None
#     health_points: None
    
#     def display(self):
#         if self.health_points >= 50:
#             print(":)") 
#         elif self.health_points > 0:
#             print("0_o")
#         else:
#             print("x_x")

# Geralt = Character()
# Geralt.name = "Geralt"
# Geralt.health_points = 100

# Geralt.display()

class Character:
    name: None
    health_points: None

    def __init__(self, p_name):
        self.name = p_name
        self.health_points = 100
    
    def display(self):
        if self.health_points >= 50:
            print(":)") 
        elif self.health_points > 0:
            print("0_o")
        else:
            print("x_x")
            
    def damage(self, points):
        self.health_points -= points

        if self.health_points < 0:
            self.health_points = 0

    def heal(self, points):
        self.health_points = points

        if self.health_points > 0:
            self.health_points += 0

Geralt = Character("Geralt")
# Geralt.name = "geralt"
# Geralt.health_points = 100

Geralt.display()
Geralt.damage(80)
Geralt.display()
Geralt.heal(80)
Geralt.display()

