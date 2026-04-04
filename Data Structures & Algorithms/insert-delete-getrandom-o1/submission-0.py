from random import choice

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.dict)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        removed_index = self.dict[val]
        last_index = len(self.dict) - 1
        self.dict[self.list[last_index]] = removed_index
        self.list[last_index], self.list[removed_index] = self.list[removed_index], self.list[last_index]
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()