class Animal():
    def __init__(self,color, types, HP):
        self.color = color
        self.types = types
        self.HP = HP
    
    def hunt(self, time):
        self.HP = self.HP - time*5
        return self.HP
    
    def eat(self, time):
        self.HP = self.HP + time*10
        return self.HP

Tiger = Animal('Yellow and Black','Cat',12000)
print('Tiger color:',Tiger.color)
print('Tiger types:',Tiger.types)
print('Tiger HP:',Tiger.HP)


#hunt:10min
print('After Hunt Tiger Hp',Tiger.hunt(10))

#eat:20min
print('After Eat Tiger Hp',Tiger.eat(20))
