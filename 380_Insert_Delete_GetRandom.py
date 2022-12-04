import random

class RandomizedSet:

    def __init__(self):
        self.my_dict = dict[int, int]()
        self.my_list = []

    def insert(self, val: int) -> bool:
        # print(f"insert {val}, list={self.my_list}, dict={self.my_dict}")
        if val in self.my_dict:
            return False
        self.my_list.append(val)
        self.my_dict[val] = len(self.my_list) - 1
        return True

    def remove(self, val: int) -> bool:
        # print(f"remove {val}, list={self.my_list}, dict={self.my_dict}")
        if val not in self.my_dict:
            return False
        idx = self.my_dict[val]
        del self.my_dict[val]
        if idx != len(self.my_list) - 1:
            val2 = self.my_list.pop()
            self.my_dict[val2] = idx
            self.my_list[idx] = val2
        else:
            self.my_list.pop()
        return True

    def getRandom(self) -> int:
        # print(f"list={self.my_list}, dict={self.my_dict}")
        list_len = len(self.my_list) - 1
        return self.my_list[random.Random().randint(0, list_len)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
