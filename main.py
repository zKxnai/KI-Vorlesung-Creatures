import numpy


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
        return ("Twins")
    else:
        return ("No Twins")


class Board:
    numpy.empty((80, 24), dtype=object)
    def __init__(self):
        self.board = np.empty((80, 24), dtype=object)
        for i in range(80):
            for j in range(24):
                self.board[i][j] = Grass("Grass")


if __name__ == "__main__":
    Wheatblock = Grass("Grass")
    Cow = Cow("MuuuKuh")
    Wolf = Wolf("Wuffi")



    #print(f"{Wheatblock.name} has {Wheatblock.hp} hp with ID {Wheatblock.id}")
    #print(f"{Cow.name} has {Cow.hp} hp with ID {Cow.id}")
    #print(f"{Wolf.name} has {Wolf.hp} hp with ID {Wolf.id}")
    #print(equals(Cow, Wolf))



