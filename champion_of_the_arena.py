from game_assetes.character import Player
from game_assetes.place import Shop, Tavern, Arena

import os

import time


def _clear():
    os.system('clear')


class ChampionOfTheArena:
    def __init__(self):
        self.enemy = None
        self.npc = None
        self.player = None
        self.shop = Shop()
        self.arena = Arena()
        self.tavern = Tavern()

        self.intro()
        time.sleep(1)
        _clear()
        self.create_player()
        time.sleep(4)
        _clear()
        self.menu()
        _clear()

    def intro(self):
        print("*" * 10, "Üdvözöllek Kalandozó", "*" * 10)

    def create_player(self):
        self.player = Player().create()
        print(f"Légy üdvözölve {self.player.name} az/a {self.player.faj} harcos  gold {self.player.gold} ")

    def menu(self):

        print("Hová akarsz menni ?")

        choises = [
            [1, "Taverna"],
            [2, "Bolt"],
            [3, "Aréna"]
        ]
        for k, v in choises:
            print(k, v)

        player_choice = input(": ")

        if player_choice == "1":
            Tavern().enter(self.player, self.npc)

        if player_choice == "2":
            Shop().enter(self.player, self.npc)

        if player_choice == "3":
            Arena().enter(self.player, self.npc)


if __name__ == '__main__':
    ChampionOfTheArena()
