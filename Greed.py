print("Greed")
import random

print("Greed")

class Falling_row:
    def generate_row():
        gem_row = [' '] * 100
        gem = random.randint(0,99)
        rock = random.randint(0,99)
        gem_row[gem] = '*'
        gem_row[rock] = 'O'
        return gem_row
    
    def print_row():
        gem_row = Falling_row.generate_row()
        for character in gem_row:
            print(character, end = '')

for i in range(15):
    Falling_row.print_row()

