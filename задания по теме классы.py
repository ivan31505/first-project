class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name, "лает!")
dog1 = Dog ("бобик",4)
dog2 = Dog("шарик", 5)
dog1.bark()


#задание 2
#оценки итоговые
##def average(self):
##    return sum(self.grades) / len(self.grades)
##student1 = Student("Аня", [5,4,3,2,1])
##student2 = Student("Вася", [5,5,2,4,3,5])

# задание  3
##class Player:
##    def __init__(self,name):
##        self.name = name
##        self.hp = 10
##        print(self.name)
##    def hit(self):
##        self.hp -= 10
##        print(self.name, "получил урон")
##
##    def heal(self):
##        self.hp += 5
##        print(self.name, "восстановил здоровье")
##
##    def show_hp(self):
##        self.hp += 5
##        print("Здоровье:",self.hp)
##p = Player("Mega hero")
##p2 = Player("Нубас")
##p.hit()
##p.hit()
##p.heal
##p.heal
##p.show_hp()


#задание 4, взаимодействие обьектов между собой
# Игрок  и враг
Class Enemy:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

    def take_damage(self,damage)
        self.hp -= damage
        
    
