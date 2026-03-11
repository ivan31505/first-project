class Player:
    def __init__(self,name, health):
        self.name = name
        self.health = health


    def show_info(self):
        print(f"Игрок: {self.name}, здоровье: {self.health}")
