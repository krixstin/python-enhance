class SoccorPlayer(object):
    #built-in special def
    def __init__(self, name : str, position : str, back_number :input):
        self.name = name
        self.position = position
        self.back_number = back_number
    
    def __str__(self):
        return "Hi, I'm {0}".format(self.name) 

    def __add__(self, other):
        return self.name + other.name

    #unique def
    def change_back_number(self, new_number):
        self.back_number=new_number
        return "{0}'s back_number has been changed to {1}".format(self.name, self.back_number)
     

kim = SoccorPlayer("Kim", 'MF', 88)
park = SoccorPlayer("Park", 'WF', 20)

print(kim.change_back_number(99))
print(kim.back_number)
print(kim+park)
