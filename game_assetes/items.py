import time

import os


def _clear():
    os.system('clear')


class Item:
    def __init__(self):
        self.price = None
        self.player = None

    def lista(self, player):
        self.player = player

    def buy(self, player):
        self.player = player

    def re_buy(self, player):
        self.player = player

    def menu(self, player):
        self.player = player

    def exit(self, player):
        self.player = player

    def __str__(self):
        return self

    def __repr__(self):
        return self


class Weapon(Item):
    weapons = [
        ["Kard", 25, 1],
        ["Csatabárd", 25, 1],
        ["Pallos", 30, 1],
        ["Kétkezes csatabárd", 50, 1]
    ]

    def lista(self, player):

        if not self.weapons:
            print("Minden elfogyott")
            time.sleep(0.5)
            print("1. Pajzs\n2 Vért\n3. Távozom")
            v = input(": ")
            if v == "1":
                Shield().lista(player)
            if v == "2":
                Armor().lista(player)
            if v == "3":
                self.menu(player)
        else:
            for i in self.weapons:
                sor = self.weapons.index(i) + 1

                print(f"{sor}, {i[0]}, ára {i[2]}")

        self.buy(player)

    def buy(self, player):
        print(f"{player.current_gold} aranyad van !")
        time.sleep(1)
        print("Válassz !")
        elem = int(input(": "))

        for i in self.weapons:
            sor = self.weapons.index(i) + 1
            sor2 = sor - 1

            if elem == sor:
                fegyver = self.weapons[sor2][0],self.weapons[sor2][1]

                player.weapon.append(fegyver)
                self.weapons.pop(sor2)
                _clear()
                print(f"Fegyver listád")

                for i in player.weapon:
                    sor = player.weapon.index(i) + 1
                    print(f" {sor} {i[0]}")

                self.re_buy(player)

    def re_buy(self, player):
        print("Vennél még valamit ?")
        time.sleep(0.5)
        print("1. igen\n2. Páncél\n3. Pajzs\n4. Távozom")

        v = input(": ")

        if v == '1':
            self.lista(player)
        if v == "2":
            Armor().lista(player)
        if v == "3":
            Shield().lista(player)
        if v == "4":
            self.menu(player)




class Armor(Item):
    armor = [
        ["Vért", 15, 3],
        ["Sisak", 10, 2]
    ]

    def lista(self, player):

        if not self.armor:
            print("Minden elfogyott")
            time.sleep(0.5)
            print("1. Fegyver\n2. Pajzs\n3. Távozom")
            v = input(": ")

            if v == "1":
                Weapon().lista(player)
            if v == "2":
                Shield().lista(player)
            if v == "3":
                self.menu(player)

        else:
            for i in self.armor:
                sor = self.armor.index(i) + 1

                print(f"{sor}, {i[0]}, ára {i[2]}")

        self.buy(player)

    def buy(self, player):
        print(f"{player.current_gold} aranyad van !")
        time.sleep(1)
        print("Válassz !")
        elem = int(input(": "))

        for i in self.armor:
            sor = self.armor.index(i) + 1
            sor2 = sor - 1

            if elem == sor:
                arm = self.armor[sor2][0], self.armor[sor2][1]

                player.armor.append(arm)
                self.armor.pop(sor2)
                _clear()

                print("Páncél  listád")

                for i in player.armor:
                    sor = player.armor.index(i) + 1
                    print(f" {sor} {i[0]}")

                self.re_buy(player)

    def re_buy(self, player):
        print("Vennél még valamit ?")
        time.sleep(0.5)
        print("1. igen\n2. Fegyver\n3. Pajzs\n4. Távozom")

        v = input(": ")

        if v == '1':
            self.lista(player)
        if v == "2":
            Weapon().lista(player)
        if v == "3":
            Shield().lista(player)
        if v == "4":
            self.menu(player)

class Shield(Item):
    shields = [
        ["Kicsi", 10, 2],
        ["Közepes", 15, 4],
        ["Nagy", 20, 8]
    ]

    def lista(self, player):

        if not self.shields:
            print("Minden elfogyott")
            time.sleep(0.5)
            print("1. Fegyver\n2. Vért\n3. Távozom")
            v = input(": ")

            if v == "1":
                Weapon().lista(player)
            if v == "2":
                Armor().lista(player)
            if v == "3":
                self.menu(player)

        else:
            for i in self.shields:
                sor = self.shields.index(i) + 1

                print(f"{sor}, {i[0]}, ára {i[2]}")

        self.buy(player)

    def buy(self, player):
        print(f"{player.current_gold} aranyad van !")
        time.sleep(1)
        print("Válassz !")
        elem = int(input(": "))

        for i in self.shields:
            sor = self.shields.index(i) + 1
            sor2 = sor - 1

            if elem == sor:
                arm = self.shields[sor2][0], self.shields[sor2][1]

                player.shield.append(arm)
                self.shields.pop(sor2)
                _clear()

                print("Páncél  listád")

                for i in player.shield:
                    sor = player.shield.index(i) + 1
                    print(f" {sor} {i[0]}")

                self.re_buy(player)

    def re_buy(self, player):
        print("Vennél még valamit ?")
        time.sleep(0.5)
        print("1. igen\n2. Fegyver\n3. Vért\n4. Távozom")

        v = input(": ")

        if v == '1':
            self.lista(player)
        if v == "2":
            Weapon().lista(player)
        if v == "3":
            Shield().lista(player)
        if v == "4":
            self.menu(player)

class Food(Item):
    food = [
        ["Sült", 2],
        ["Ragu", 2],
        ["Kenyér", 1],
        ["Szalonna", 1],
        ["Sajt", 1],
    ]

    def buy(self, player):
        """
        Player ha arénából jön és eszik az életereje vissza tötődik
        :param player:
        :return:
        """
        print(f"{player.current_gold} aranyad van !")
        time.sleep(1)
        print("Mit ennél ?")
        for i in self.food:
            sor = self.food.index(i) + 1

            print(f"{sor}, {i[0]}, ára {i[1]}")

        valasz = int(input(": "))

        for i in self.food:
            sor = self.food.index(i) + 1

            if valasz == sor:
                if player.current_gold > self.food[sor - 1][1]:
                    player.current_gold -= self.food[sor - 1][1]
                    print(f"itt a {i[0]} Jó étvágyat !")
                    time.sleep(1)
                    player.current_hp = player.hp
                    print(f"Élert erőd maximumon {player.current_hp}")
                    time.sleep(1)
                    _clear()
                    print("Hozzhatok még valamit?")
                    print("1. Étel\n2. Itall\n3. Távozol")
                    valasz = input(": ")

                    if valasz == "1":
                        Food().buy(player)
                        _clear()
                    if valasz == "2":
                        Drink().buy(player)
                        _clear()
                    if valasz == "3":
                        self.exit(player)
                        _clear()



                else:
                    print(f"Neked csak {player.current_gold} aranyad van !")
                    self.menu(player)
                    _clear()


class Drink(Item):
    drink = [
        ["Sör", 1],
        ["Bor", 1],
        ["Pálinka", 2]
    ]

    def buy(self, player):
        print(f"{player.current_gold} aranyad van !")
        time.sleep(1)
        print("Mit innál ?")
        for i in self.drink:
            sor = self.drink.index(i) + 1

            print(f"{sor}, {i[0]}, ára {i[1]}")

        valasz = int(input(": "))

        for i in self.drink:
            sor = self.drink.index(i) + 1

            if valasz == sor:
                if player.current_gold > self.drink[sor - 1][1]:
                    player.current_gold -= self.drink[sor - 1][1]
                    print(f"Itt  a {i[0]} ! Egészségedre kalandozó !")
                    time.sleep(1)

                    print("Hozzhatok még valamit?")
                    print("1. Étel\n2. itall\n3. távozol")
                    valasz = input(": ")

                    if valasz == "1":
                        Food().buy(player)
                        _clear()

                    elif valasz == "2":
                        Drink().buy(player)
                        _clear()

                    elif valasz == "3":
                        self.exit(player)
                        _clear()


                else:
                    print(f"Neked csak {player.current_gold} aranyad van !")
                    self.menu(player)
                    _clear()




if __name__ == '__main__':
    pass
