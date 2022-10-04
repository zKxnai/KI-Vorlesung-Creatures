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


class Animal(Creatures):
    def __init__(self, name):
        """print("Constructor of Class Animal")"""
        super().__init__(name)
        self.hp = 0


class Cow(Animal):
    def __init__(self, name):
        """print("Constructor of Class Cow")"""
        super().__init__(name)
        self.hp = 200


class Wolf(Animal):
    def __init__(self, name):
        """print("Constructor of Class Wolf")"""
        super().__init__(name)
        self.hp = 100


def equals(typea, typeb):
    if typea.__class__ == typeb.__class__:
        return "Twins"
    else:
        return "No Twins"


class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = [[" " for i in range(y)] for j in range(x)]

    def add(self, creatures, x, y):
        if x < self.x and y < self.y:
            self.board[x][y] += creatures.name
        else:
            print("Out of range")

    def get(self, x, y):
        if x < self.x and y < self.y:
            return self.board[x][y]
        else:
            print("Out of range")

    def remove(self, x, y):
        if x < self.x and y < self.y:
            self.board[x][y] = None
        else:
            print("Out of range")

    def printboard(self):
        boardstring = ""
        for i in range(self.x):
            for j in range(self.y):
                #print(self.board[i][j], end=" ")
                boardstring += self.board[i][j] + " "
            #print()
            boardstring += "\n"
        return boardstring


if __name__ == "__main__":
    grass = Grass("G")
    paula = Cow("C")
    wuffi = Wolf("W")


    board = Board(24, 80)
    board.add(paula, 0, 0)
    board.add(wuffi, 1, 1)
    board.add(grass, 2, 0)

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
        time.sleep(2)
        board.add(grass, 14, 50)
        print("\033[H" + board.printboard())

