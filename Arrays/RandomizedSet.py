import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val):
        if val in self.pos:
            return False

        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val):
        if val not in self.pos:
            return False

        i = self.pos[val]
        last = self.arr[-1]

        self.arr[i] = last
        self.pos[last] = i

        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        return random.choice(self.arr)