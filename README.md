# AI-Lecture-Creatures
Python Programm für die Übungsaufgabe, die aufeinander aufbauen.

## Übung 1
Erstellung des Programms mit Klassen für Creatures, Animal, Grass, Cow und Wolf. Die Klassen Grass und Animal erben von Creatures. Die Klassen Cow und Wolf erben von Animal und somit auch vo Creatures.

Beispiel:  
```
print(f"{Grassblock.name} has {Grassblock.hp} hp with ID {Grassblock.id}")
Grass has 50 hp with ID 0b70149e-40b1-11ed-b1a7-0a7d754545ac
```

## Übung 2
Erstellung eines Vergleichs zwischen den Klassen mit einer Ausgabe, ob die vergleichten Klassen übereinstimmen oder nicht.

Beispiel:  
```
print(equals(muuukuh, wuffi))
No Twins
```

## Übung 3
Erweitern durch ein 80x24 Grid, wobei jede Zelle eine Liste von Creatures beinhaltet.

Beispiel:  
```
board.printboard()
[Paula] [HanZ] ... [None] [None] 
[None] [None] ... [None] [None] 
[None] [None] ... [None] [None]  
[None] [None] ... [None] [None]  
[None] [None] ... [None] [None] 
.
.
.
[None] [None] ... [None] [None] 
[None] [None] ... [None] [None]  
[None] [None] ... [None] [None]  
[None] [None] ... [None] [None]
