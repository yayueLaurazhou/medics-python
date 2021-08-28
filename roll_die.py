# random is the name of the module, randint is te name of the method
from random import randint

# Represent a die, which can be rolled.
class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


d6 = Die(6)

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print(f"10 rolls of a 6-sided die: {results}")


