import os
import time

class Creatures:
    def __init__(self, name):
        """print("Constructor of Class Creatures")"""
        self.name = name
        self.hp = 0
        from uuid import uuid1
        self.id = uuid1()


class Grass(Creatures):
    def __init__(self, name):
        """print("Constructor of Class Grass")"""
        super().__init__(name)
        self.hp = 50
        self.value = 1


class Animal(Creatures):
    def __init__(self, name):
        """print("Constructor of Class Animal")"""
        super().__init__(name)
        self.hp = 0

    def moveRequest(self):
        print(self.name + " sent a move request")


class Cow(Animal):
    def __init__(self, name):
        """print("Constructor of Class Cow")"""
        super().__init__(name)
        self.hp = 200
        self.value = 2


class Wolf(Animal):
    def __init__(self, name):
        """print("Constructor of Class Wolf")"""
        super().__init__(name)
        self.hp = 100
        self.value = 3


def equals(typea, typeb):
    if typea.__class__ == typeb.__class__:
        return "Twins"
    else:
        return "No Twins"


class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.boardField = {}

        for i in range(self.y):
            for j in range(self.x):
                self.boardField[j, i] = []

    def add(self, creatures, x, y):
        if x <= self.x and y <= self.y:
            self.boardField[x, y].append(creatures)
        else:
            print("Out of range")

    #def get(self, x, y):
        #if x < self.x and y < self.y:
            #return self.boardField[x][y]
        #else:
            #print("Out of range")

    def remove(self, x, y):
        if x <= self.x and y <= self.y:
            for creatures in self.boardField[x, y]:
                self.boardField[x, y].pop()
        else:
            print("Out of range")

    def printboard(self):
        boardString = ""
        for i in range(self.y):
            boardString += "\n"
            for j in range(self.x):
                if len(self.boardField[j, i]) > 0:
                    highestCreature = max(content.value for content in self.boardField[j, i])
                    if highestCreature == 1:
                        boardString += "P"
                    elif highestCreature == 2:
                        boardString += "C"
                    elif highestCreature == 3:
                        boardString += "W"
                    else:
                        print("Error")
                else:
                    boardString += "."
        boardString += "\n"
        return boardString


if __name__ == "__main__":
    grass = Grass("P")
    paula = Cow("C")
    wuffi = Wolf("W")
    tics = 2


    board = Board(80, 24)
    board.add(paula, 0, 0)
    board.add(wuffi, 1, 1)
    board.add(grass, 2, 0)

    print()

    os.system("clear")

    #print("\033[1m" + "\033[4m" + "Infos über Creatures" + "\033[0m")
    #print(f"{grass.name} has {grass.hp} hp with ID {grass.id}")
    #print(f"{paula.name} has {paula.hp} hp with ID {paula.id}")
    #print(f"{wuffi.name} has {wuffi.hp} hp with ID {wuffi.id}")
    #print()
    #print("\033[1m" + "\033[4m" + "Infos über Vergleich" + "\033[0m")
    #print(equals(paula, wuffi))
    #print()
    #print("\033[1m" + "\033[4m" + "Infos über Board" + "\033[0m")
    #board.printboard()

    while True:
        time.sleep(tics)
        print("\033[H" + board.printboard())

        board.add(grass, 50, 20)

