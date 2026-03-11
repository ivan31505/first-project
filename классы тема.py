#class описывает кике данные и действия есть у обьекта
#обьект - это экземпляр класса

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def meow(self):
        print(self.name, "говорит: мяу")

    def golod(self):
        print(self.name,"хочет есть")

cat1 = Cat("Барсик", 3)
cat2 = Cat("матроскин", 60)

print(cat1.name)
print(cat2.age)
##print(cat2.name)
##print(cat1.age)

cat1.meow()
cat2.meow()
cat2.golod()
cat1.golod()
