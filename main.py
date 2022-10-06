import os
import time
from random import randrange


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

    def randomMoveRequest(self, x, y, sizeX, sizeY):
        match randrange(4):
            case 0:  # left
                if x - 1 == -1:  # too far => go to other end
                    return sizeX - 1, y
                else:
                    return x - 1, y
            case 1:  # right
                if x + 1 == sizeX:  # too far => go to other end
                    return 0, y
                else:
                    return x + 1, y
            case 2:  # down
                if y + 1 == sizeY:  # too far => go to other end
                    return x, 0
                else:
                    return x, y + 1
            case 3:  # up
                if y - 1 == -1:  # too far => go to other end
                    return x, sizeY - 1
                else:
                    return x, y - 1


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


def movedAnimals():
    movedAnimals = []
    for i in range(board.y):
        for j in range(board.x):
            k = 0
            while k < len(board.boardField[j, i]):
                if (board.boardField[j, i][k].value == 2 or board.boardField[j, i][k].value == 3):
                    x, y = board.boardField[j, i][k].randomMoveRequest(j, i, board.x, board.y)
                    creaturesToMove = board.boardField[j, i].pop(k)
                    k -= 1
                    movedAnimals.append([x, y, creaturesToMove])
                k += 1
    for i in range(len(movedAnimals)):
        board.add(movedAnimals[i][2], movedAnimals[i][0], movedAnimals[i][1])


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
                        boardString += "🍒"  # Grass
                    elif highestCreature == 2:
                        boardString += "😱"  # Cow
                    elif highestCreature == 3:
                        boardString += "👻"  # Wolf
                    else:
                        print("Error")
                else:
                    boardString += "⬛️"
        boardString += "\n"
        return boardString

def first(iterable, conditions=lambda x: True):
    try:
        return next(x for x in iterable if conditions(x))
    except StopIteration:
        return None

def hunting():
    for i in range(board.y):
        for j in range(board.x):
            if len(board.boardField[j, i]) > 1:
                highestCreature = max(content.value for content in board.boardField[j, i])
                if highestCreature == 3:
                    foundwolf, foundcow = False, False
                    for creatures in board.boardField[j, i]:
                        if not foundcow:
                            if creatures.value == 2:
                                board.boardField[j, i].remove(creatures)
                                killed.append(creatures)
                                #print("\033[27;1HWolf killed a cow.")
                                foundcow = True
                        if not foundwolf and first(board.boardField[j, i], lambda x: x.value == 2):
                            if creatures.value == 3:
                                if creatures.hp < 200:
                                    creatures.hp += 50
                                foundwolf = True
                elif highestCreature == 2:
                    foundcow, foundgrass = False, False
                    for creatures in board.boardField[j, i]:
                        if not foundgrass:
                            if creatures.value == 1:
                                if creatures.hp > 5:
                                    creatures.hp -= 5
                                else:
                                    board.boardField[j, i].remove(creatures)
                                    killed.append(creatures)
                                    #print("\033[27;1HCow ate some grass.")
                                foundgrass = True
                        if not foundcow and first(board.boardField[j, i], lambda x: x.value == 1):
                            if creatures.value == 2:
                                if creatures.hp < 400:
                                    creatures.hp += 10
                                foundcow = True


def transformKilled():
    returnString = ""
    strWolf = 0
    strCow = 0
    strGrass = 0

    for i in range(len(killed)):
        if killed[i].value == 3:
            strWolf += 1
        elif killed[i].value == 2:
            strCow += 1
        elif killed[i].value == 1:
            strGrass += 1

    return returnString + "Ghosts: " + str(strWolf) + " Pacman: " + str(strCow) + " Cherries: " + str(strGrass)

def AnimalHP():
    for i in range(board.y):
        for j in range(board.x):
            for creatures in board.boardField[j, i]:
                print(creatures.name + " HP: " + str(creatures.hp) + "\033[K")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    killed = []

    #Creating the board and content
    board = Board(80, 24)
    board.add(Cow("Pacman"), 2, 2)
    board.add(Grass("Cherry"), 2, 1)
    board.add(Grass("Cherry"), 25, 10)
    board.add(Grass("Cherry"), 58, 17)
    for i in range(4):
        board.add(Wolf("Ghost"), 35, i)

    print()

    #Printing board and content with functions
    while True:
        time.sleep(0.01)

        movedAnimals()
        hunting()
        transformKilled()
        print("\033[H\033[1m\033[4mBoardgame\n\033[K\033[0m" + board.printboard()
              + "\n\nKilled following animals: "+ transformKilled())
        AnimalHP()