class MyHashSet:

    POW = 9811
    MOD = 10000

    def __init__(self):
        self.storage = [list[int]() for _ in range(MyHashSet.MOD)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.storage[key * MyHashSet.POW % MyHashSet.MOD].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.storage[key * MyHashSet.POW % MyHashSet.MOD].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.storage[key * MyHashSet.POW % MyHashSet.MOD]


# Your MyHashSet object will be instantiated and called as such:
key = 7
obj = MyHashSet()
obj.add(key)
obj.remove(key)
param_3 = obj.contains(key)
print(param_3)