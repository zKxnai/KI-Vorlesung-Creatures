#import numpy


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
        self.board = [["[None]" for i in range(y)] for j in range(x)]

    def add(self, creatures, x, y):
        if x < self.x and y < self.y:
            self.board[x][y] = "[" + creatures.name + "]"
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

    def __str__(self):
        return str(self.board)

    def __repr__(self):
        return str(self.board)

    def printboard(self):
        for i in range(self.x):
            for j in range(self.y):
                print(self.board[i][j], end=" ")
            print()


if __name__ == "__main__":
    Grassblock = Grass("Grass")
    muuukuh = Cow("MuuuKuh")
    paula = Cow("Paula")
    wuffi = Wolf("Wuffi")
    hanz = Wolf("HanZ")
    board = Board(80, 24)
    board.add(paula, 0, 0)
    board.add(hanz, 0, 1)

    print("\033[1m" + "\033[4m" + "Infos über Creatures" + "\033[0m")
    print(f"{Grassblock.name} has {Grassblock.hp} hp with ID {Grassblock.id}")
    print(f"{muuukuh.name} has {muuukuh.hp} hp with ID {muuukuh.id}")
    print(f"{wuffi.name} has {wuffi.hp} hp with ID {wuffi.id}")
    print()
    print("\033[1m" + "\033[4m" + "Infos über Vergleich" + "\033[0m")
    print(equals(muuukuh, wuffi))
    print()
    print("\033[1m" + "\033[4m" + "Infos über Board" + "\033[0m")
    board.printboard()
