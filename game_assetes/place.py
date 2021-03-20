from game_assetes.character import Enemy, NPC, Champion
from game_assetes.items import Weapon, Armor, Food, Drink, Shield

import time
import os


def _clear():
    os.system('clear')


class Place:

    def __init__(self):
        self.target = None
        self.enemy = Enemy().create()
        self.npc = NPC().create()
        self.player = None
        self.weapon = Weapon()
        self.armor = Armor()
        self.food = Food()
        self.drink = Drink()
        self.shield = Shield()

        self.bet_gold = None

    def enter(self, player, npc):
        self.player = player
        self.npc = npc
        _clear()

    def exit(self, player):
        self.player = player
        self.menu()
        _clear()

    def champ(self, player):
        self.player = player
        return self

    def enemy_create(self):
        Enemy().create()
        return self

    def npc(self):
        NPC().create()
        return self

    def jatek(self, player, npc):
        self.player = player
        self.npc = npc

    def bet(self, player):
        self.player = player
        print("Tedd meg a tétet !")
        tet = int(input(": "))

        if player.current_gold < tet:
            print("Nincs elég pénzed !")
            print("1. Tegyél  kisseb összeget\n2 Vagy távozz !")
            valasz = input(": ")

            if valasz == "1":
                tet = int(input(": "))
                self.bet_gold = tet

            if valasz == "2":
                self.menu()

            if valasz > "2" or valasz < "1" or valasz == "":
                self.bet(player)


        else:
            self.bet_gold = tet

        _clear()

    def menu(self):
        print("1. Taverna\n2. Bolt\n3. Aréna")

        player_choice = input(": ")

        if player_choice == "1":
            Tavern().enter(self.player, self.npc)
            _clear()

        if player_choice == "2":
            Shop().enter(self.player, self.npc)
            _clear()

        if player_choice == "3":
            Arena().enter(self.player, self.npc)
            _clear()

        if player_choice > "3" or player_choice < "1":
            print("A listából válassz !")
            self.menu()


class Arena(Place):
    champ1 = Champion().create("Farbatosz ", "Dwarf", 50, 30)
    champ2 = Champion().create("Legolas", "Elf", 40, 40)
    champ3 = Champion().create("Urgot", "Ork", 60, 20)
    champ4 = Champion().create("Sir Elton Jhone", "Human", 70, 50)

    champions = [champ1, champ2, champ3, champ4]

    def enter(self, player, npc):
        npc = "Jerry Spencer"

        print(f"Üdvözöllek {player} harcos a nevem {npc} az aeréna mester ")
        print("1. Harcolsz\n2. Bajnokot\n3 Távozol")
        valasz = int(input(": "))

        if valasz == 1:
            print("Válaszd ki a felszerésed amiben harcolni akarsz")
            self.item_select(player)
        if valasz == 2:
            self.champ(player)

        if valasz == 3:
            self.menu()

        if valasz > 2 or valasz < 1:
            print("A listából válassz !")
            self.enter(self, player)

    def champ(self, player):
        print("Válassz a bajnokok közül !")

        for i in self.champions:
            sor = self.champions.index(i) + 1
            print(sor, i)

        v = int(input(": "))

        for i in self.champions:
            sor = self.champions.index(i) + 1
            sor2 = sor - 1

            if v == sor:
                pass




    def item_select(self, player):
        print("1. Páncél\n2. Fegyver\n3. Pajzs\n4. Harcolsz\n5. Távozol")
        valasz = input(": ")

        if valasz == "1":
            self.armor_select(player)
        if valasz == "2":
            self.weapon_select(player)
        if valasz == "3":
            self.shield_select(player)
        if valasz == "4":
            self.csata(player, self.enemy)
        if valasz == "5":
            self.menu()

        if valasz > "5" or valasz < "1" or valasz == "":
            print("A listából válassz !")
            self.item_select(player)

    def weapon_select(self, player):
        """
        A player kiválaszthaja fegyverét amivel harcolni akar és a támadó értéke
        hozzá adodik a playeréhez
        :param player:
        :return:
        """
        if not player.weapon:
            print("Nincs fegyvered !")
            print("1. Páncél\n2. Pajzs\n3. Harcolsz\n4. Távozol")
            valasz = input(": ")

            if valasz == "1":
                self.armor_select(player)
            if valasz == "2":
                self.shield_select(player)
            if valasz == "3":
                self.csata(player, self.enemy)
            if valasz == "4":
                self.menu()

            if valasz > "5" or valasz < "1" or valasz == "":
                print("A listából válassz !")
                self.item_select(player)


        else:

            for i in player.weapon:
                sor = player.weapon.index(i) + 1

                print(f"{sor}, {i[0]}")

            v = int(input(": "))

            for i in player.weapon:
                sor = player.weapon.index(i) + 1

                if v == sor:
                    player.right_hand.append(i[1])

            for i in player.right_hand:
                player.attack_power = player.ero + i
            self.item_select(player)

    def armor_select(self, player):
        """
        A harchoz kiválaszthatja, a player a védő felszerelését
        aminek védő értéke hozzá adodik a player védőjéhez
        :param player:
        :return:
        """

        if not player.armor:
            print("Nincs vérted")
            print("1. Fegyver\n2. Pajzs\n3. Harcolsz\n4. Távozol")
            valasz = input(": ")

            if valasz == "1":
                self.weapon_select(player)
            if valasz == "2":
                self.shield_select(player)
            if valasz == "3":
                self.csata(player, self.enemy)
            if valasz == "4":
                self.menu()

            if valasz > "5" or valasz < "1" or valasz == "":
                print("A listából válassz !")
                self.item_select(player)
        else:

            for i in player.armor:
                sor = player.armor.index(i) + 1

                print(f"{sor}, {i[0]}")

            v = int(input(": "))

            for i in player.armor:
                sor = player.armor.index(i) + 1

                if v == sor:
                    player.body.append(i[1])
                    self.item_select(player)
        cover = 0
        for i in player.body:
            cover += i
            player.protection = player.cover + cover
            print(player.protection)

    def shield_select(self, player):

        if not player.shield:
            print("Nincs pajzsod")
            print("1. Páncél\n2. Fegyver\n3. Halcolsz\n4. Távozol")
            valasz = input(": ")

            if valasz == "1":
                self.armor_select(player)
                _clear()
            if valasz == "2":
                self.weapon_select(player)
                _clear()
            if valasz == "3":
                self.csata(player, self.enemy)
                _clear()
            if valasz == "4":
                self.menu()
                _clear()

            if valasz > "2" or valasz < "1" or valasz == "":
                print("A listából válassz !")
                self.armor_select(player)
        else:
            for i in player.right_hand:
                if i >= 30:
                    print("Kétkezes fegyvered van nem lehet pajzsod")
                    print("1. Páncél\n2 Harcolsz\n3 Távozol")
                    v = input(": ")
                    if v == "1":
                        self.armor_select(player)
                    if v == "2":
                        self.csata(player, self.enemy)
                    if v == "3":
                        self.menu()
                else:
                    for i in player.shield:
                        sor = player.shield.index(i) + 1

                        print(f"{sor}  {i[0]}")

                    v = int(input(": "))

                    for i in player.shield:
                        sor = player.shield.index(i) + 1
                        if v == sor:
                            player.left_hand.append(i[1])

            for i in player.left_hand:
                player.protection = player.cover + i
                print(player.protection)
                self.armor_select(player)

    def csata(self, player, enemy):
        win = 0
        los = 0
        print(f"Az ellen feled {self.enemy.name} aki egy {self.enemy.faj}  harcos !")
        print("1. Fogasz\n2 Harc")
        v = input(": ")

        if v == "1":
            self.bet(player)

            while True:
                player.attack(enemy)
                time.sleep(2)
                enemy.attack(player)
                time.sleep(2)

                if enemy.current_hp < 20:
                    win += 1
                    print("Győztél !")
                    player.current_gold += self.bet_gold * 2
                    time.sleep(0.5)
                    print(f"{self.bet_gold} értékben fogattál ,így {player.current_gold} aranyad van")
                    time.sleep(1)
                    print(f"Ez a {win}  győzelmed !")

                    time.sleep(1)
                    self.menu()
                    _clear()

                if player.current_hp < 40:
                    los += 1
                    print("Vesztettél !")
                    player.current_gold -= self.bet_gold
                    print(f"{self.bet_gold} összeggel fogadttál maradt {player.current_gold} aranyad ")
                    time.sleep(1)
                    print(f"Ez a {los}  vereséged !")

                    time.sleep(1)
                    self.menu()
                    _clear()

        if v == "2":

            while True:
                player.attack(enemy)
                time.sleep(2)
                enemy.attack(player)
                time.sleep(2)

                if enemy.current_hp < 20:
                    win += 1
                    print("Győztél !")
                    time.sleep(1)
                    print(f"Ez a {win}  győzelmed !")

                    time.sleep(1)
                    self.menu()
                    _clear()

                if player.current_hp < 40:
                    los += 1
                    print("Vesztettél !")
                    time.sleep(1)
                    print(f"Ez a {los}  vereséged !")

                    time.sleep(1)
                    self.menu()
                    _clear()




class Shop(Place):

    def __init__(self):
        super().__init__()

    def enter(self, player, npc):
        npc = "Robert Cochran"

        print(f"Üdvözöllek  {player} a nevem {npc}")
        time.sleep(1)
        print("Mit vennél\n1. Fegyver\n2. Vért\n3. Pajzs\n4. Semmit ")
        valasz = input(": ")

        if valasz == "1":
            Weapon().lista(player)
            self.exit(player)
            _clear()

        if valasz == "2":
            Armor().lista(player)
            self.exit(player)
            _clear()

        if valasz == "3":
            Shield().lista(player)
            self.exit(player)
            _clear()

        if valasz == "4":
            self.exit(player)
            _clear()

        if valasz > "4" or valasz < "1" or valasz == "":
            print("A listából válasz!")
            self.enter(player, npc)


class Tavern(Place):
    def __init__(self):
        super().__init__()

    def jatek(self, player, npc):
        self.player = player
        print(f"Ügvözöllek a nevem {self.npc.name}")
        print("Biztos nálam akarod hagyni a goldod?")
        print("1. Igen\n2. Nem")
        valasz = input(": ")

        if valasz > "2" or valasz < "1" or valasz == "":
            valasz = input(": ")

        if valasz == "1":
            self.game(player, npc)
            _clear()

        if valasz == "2":
            self.enter(player, npc)
            _clear()

    def game(self, player, npc):
        print(f"{player.current_gold} aranyad van !")

        self.bet(player)

        print("A te dobásod ")
        player.score(player)
        time.sleep(0.5)
        print(f"{self.npc.name} dobása ")
        npc.score(self.npc)
        time.sleep(0.5)

        if player.win_hand > self.npc.win_hand:
            player.current_gold += self.bet_gold * 2
            print(f"{player} nyert ")

            player.win_hand.clear()
            self.npc.win_hand.clear()

        elif player.win_hand == self.npc.win_hand:
            print("Döntetlen !")

            player.win_hand.clear()
            self.npc.win_hand.clear()
        else:
            player.current_gold -= self.bet_gold
            print(f"{self.npc.name} nyert!")
            time.sleep(0.5)
            print(f"{player.current_gold} aranyad maradt")
            player.win_hand.clear()
            self.npc.win_hand.clear()

        print("Még egy játék?")
        print("1. Igen\n2. Nem")
        valasz = input(": ")

        if valasz > "2" or valasz < "1" or valasz == "":
            valasz = input(": ")

        if valasz == "1":
            self.game(player, npc)
            _clear()
        if valasz == "2":
            self.enter(player, npc)
            _clear()

    def enter(self, player, npc):
        npc = "Stacey Hahn"

        print(f"Üdv {player.name} a nemvem {npc} !")
        time.sleep(1)
        print(f"Mivel szolgálhatok \n1. Étel\n2. ital\n3. kocka\n4 távozol ?")
        valasz = input(": ")

        if valasz == "1":
            Food().buy(player)
            self.exit(player)
            _clear()
        elif valasz == "2":
            Drink().buy(player)
            self.exit(player)
            _clear()
        elif valasz == "3":
            self.jatek(player, self.npc)
            _clear()
        elif valasz == "4":
            self.exit(player)
            _clear()

        if valasz > "2" or valasz < "1" or valasz == "":
            print("A listából válassz !")
            self.enter(player, npc)


if __name__ == '__main__':
    pass
