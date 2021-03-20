import random
from faker import Faker

fake = Faker()

fajok = ["Human", "Törpe", "Elf", "Ork"]

for faj in fajok:

    if faj == "Human":
        ero = random.randint(10, 20)
        cover = random.randint(15, 30)
    elif faj == "Dwarf":
        ero = random.randint(15, 25)
        cover = random.randint(10, 20)
    elif faj == "Ork":
        ero = random.randint(15, 28)
        cover = random.randint(10, 15)
    elif faj == "Elf":
        ero = random.randint(10, 15)
        cover = random.randint(15, 30)


class Character:
    fajok = ["Human", "Dwarf", "Elf", "Ork"]

    def __init__(self):
        self.name = None
        self.faj = None

        self.gold = random.randint(5, 15)
        self.current_gold = self.gold

        self.hp = 100
        self.current_hp = self.hp

        self.ero = ero
        self.attack_power = self.ero

        self.cover = cover
        self.protection = self.cover

        self.weapon = []
        self.armor = []
        self.shield = []

        self.right_hand = []
        self.left_hand = []
        self.body = []
        self.win_hand = []

    def create(self, name, faj):
        self.name = name
        self.faj = faj

        return self

    def attack(self, target):
        r_attack = random.randint(2, 12)
        attack_strength = (r_attack + self.attack_power) - self.protection

        if attack_strength == 0:
            print(
                f"{self.name}  támadja  {target.name} . Ellenfél kivédte ! Védő: {target.protection}  Támadás : {attack_strength}")
        if attack_strength < target.protection:
            print(
                f"{self.name}  támadja  {target.name} . A csapás mellément ! Védő: {target.protection}  Támadás : {attack_strength} ")
        if attack_strength > target.protection:
            print(f"{self.name} támadja  {target.name} . A támadás ereje {attack_strength} ")
            target.current_hp -= attack_strength
            print(f"{target.name}  élete  : {target.current_hp} maradt !")

    def score(self, gamer):

        k = random.randint(1, 6)
        k2 = random.randint(1, 6)
        k3 = random.randint(1, 6)
        k4 = random.randint(1, 6)
        k5 = random.randint(1, 6)

        hand = [k, k2, k3, k4, k5]
        hand.sort()

        print(hand)

        counts = [0, 0, 0, 0, 0, 0, 0]
        for i in hand:
            counts[i] += 1
        if 5 in counts:
            self.win_hand.append(10)
            print("Five of a Kind")
        elif 4 in counts:
            self.win_hand.append(9)
            print("Póker")
        elif 3 in counts and 2 in counts:
            self.win_hand.append(8)
            print("Full")
        elif counts == [1, 2, 3, 4, 5]:
            self.win_hand.append(15)
            print("Sor")
        elif 3 in counts:
            self.win_hand.append(6)
            print("Drill")
        elif counts.count(2) == 2:
            self.win_hand.append(4)
            print("Két pár")
        elif 1 in counts:
            self.win_hand.append(1)
            print("Pár")
        elif 0 in counts:
            print("Semmi")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Player(Character):

    def create(self):
        global faj
        name = input("Mi a neved kalandozó : ")
        while name == "":
            name = input("Mi a neved kalandozó : ")

        for k in self.fajok:
            sor = self.fajok.index(k) + 1
            print(f"{sor} {k}")

        v = int(input(": "))

        for k in self.fajok:
            sor = self.fajok.index(k) + 1

            if v == sor:
                faj = k

        return super().create(name, faj)


class Enemy(Character):
    fegyver = [0, 14, 15, 30, 40]

    pajzs = [0, 10]

    test = [0, 10, 5]

    def create(self, name=None, faj=None):
        self.name = fake.name()

        self.faj = random.choice(self.fajok)

        if self.faj == "Human":
            self.ero = random.randint(10, 20)
            self.cover = random.randint(10, 30)
        elif self.faj == "Törpe":
            self.ero = random.randint(10, 25)
            self.cover = random.randint(10, 20)
        elif self.faj == "Ork":
            self.ero = random.randint(10, 28)
            self.cover = random.randint(10, 15)
        elif self.faj == "Elf":
            self.ero = random.randint(10, 15)
            self.cover = random.randint(10, 30)

        self.right_hand = random.choice(self.fegyver)

        if self.right_hand >= 30:
            self.left_hand = 0
        else:
            self.left_hand = random.choice(self.pajzs)

        self.body = self.cover + random.choice(self.test) + random.choice(self.test)

        self.attack_power = self.ero + self.right_hand

        self.protection = self.cover + self.left_hand + self.body

        return self


class Champion(Character):
    def create(self, name, faj, attack_power, protection,):
        self.name = name
        self.faj = faj
        self.attack_power = attack_power
        self.protection = protection
        return self

class NPC(Enemy):
    pass


if __name__ == '__main__':
    pass
