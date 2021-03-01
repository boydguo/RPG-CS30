# Course: CS 30
# Period: 1
# Date created: 02/02/21
# Date last modified: 02/02/21
# Name: Boyd Guo
# Description: RPG: Modules and Maps

import random
from os import system
from characters import Person
import locations
from map import Map

# prints out the squad list
p1 = Person("David", "Blaine", "Sergeant")
p2 = Person("Ryan", "Smith", "Private")
p3 = Person("Thomas", "Miller", "Private")
p4 = Person("Christopher", "Jones", "Private")


def main():
    map = Map()
    playing = True
    while playing:
        system("clear")
        print("Squad List")
        p1.myfunc()
        p2.myfunc()
        p3.myfunc()
        p4.myfunc()
        print()
        map.print()
        print()

        while True:
            choice = input(
                "Type continue to move to the next point on the map\n"
            )
            if choice == "continue":
                break
            elif choice == "quit":
                playing = False
                break
            print("Invalid input.")

        map.position += 1


main()
