import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 120
        self.max_hp = 120
        self.critical_chance = 15
        self.xp = 0
        self.level = 1
        self.armor = 3

    def __str__(self):
        return f"{self.name}: HP {self.hp}/{self.max_hp}, Уровень {self.level}, XP {self.xp}/20, Броня {self.armor}"

    def is_alive(self):
        return self.hp > 0

    def hit(self, damage):
        blocked = min(damage, self.armor)
        actual_damage = damage - blocked
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0

        print(self.name, "получил урон:", damage)
        print("Броня блокировала:", blocked)
        print("Итого урон:", actual_damage)

        if self.hp == 0:
            print("Герой проиграл!")

    def attack(self, enemy):
        if random.randint(1, 100) <= self.critical_chance:
            damage = random.randint(25, 35)
            print(f"✨ {self.name} наносит КРИТИЧЕСКИЙ УДАР на {damage}!")
        else:
            damage = random.randint(12, 20)
            print(self.name, "атакует", enemy.name, "на", damage)
        enemy.take_damage(damage)

    def check_level_up(self):
        if self.xp >= 20:
            self.level += 1
            self.max_hp += 20
            self.hp = self.max_hp
            self.xp -= 20
            print(f"🎉 Новый уровень! Уровень: {self.level}, HP увеличено до {self.max_hp}!")


class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp

    def __str__(self):
        return f"{self.name}: HP {self.hp}/{self.max_hp}"

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(self.name, "теперь имеет HP", self.hp)
        if self.hp == 0:
            print("Слизень побеждён!")

    def attack(self, player):
        damage = random.randint(7, 13)
        print(self.name, "бьёт", player.name, "на", damage)
        player.hit(damage)

class Boss(Monster):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.super_attack_cooldown = 0

    def __str__(self):
        return f"БОСС {self.name}: HP {self.hp}/{self.max_hp} (ОПАСНОСТЬ!)"

    def super_attack(self, player):
        damage = random.randint(18, 30)
        print(f"🔥 {self.name} использует СУПЕР-АТАКУ на {player.name} на {damage} урона!")
        player.hit(damage)
        self.super_attack_cooldown = 3

    def attack(self, player):
        if (random.randint(1, 100) <= 20 and
                self.super_attack_cooldown == 0):
            self.super_attack(player)
        else:
            damage = random.randint(10, 18)
            print(self.name, "атакует", player.name, "на", damage)
            player.hit(damage)

        if self.super_attack_cooldown > 0:
            self.super_attack_cooldown -= 1

def game():
    print("=== Мини RPG ===")
    name = input("Имя героя: ")
    player = Player(name)
    boss = Boss("Дракон", 100)
    print("\nО НЕТ! Перед вами БОСС — Дракон!")

    print("\nСтарт:")
    print(player)
    print(boss)

    round_num = 1

    while player.is_alive() and boss.is_alive():
        print(f"\n--- Раунд {round_num} ---")
        input("Нажми Enter, чтобы атаковать... ")
        player.attack(boss)
        if boss.is_alive():
            boss.attack(player)
        print("\nСостояние:")
        print(player)
        print(boss)
        round_num += 1

    if player.is_alive():
        print("\n🎉 ПОБЕДА! Вы победили БОССА-ДРАКОНА!")
        player.xp += 10
        player.check_level_up()
    else:
        print("\n💀 Поражение! БОСС победил вас...")

game()
