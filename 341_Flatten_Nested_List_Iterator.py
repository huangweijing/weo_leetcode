# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def expand(self, nested_list: [NestedInteger]) -> list[int]:
        ret = []
        for val in nested_list:
            if val.isInteger():
                ret.append(val.getInteger())
            else:
                ret.extend(self.expand(val.getList()))
        return ret

    def __init__(self, nestedList: [NestedInteger]):
        self.nl = self.expand(nestedList)
        self.idx = 0

    def next(self) -> int:
        ret = self.nl[self.idx]
        self.idx += 1
        return ret

    def hasNext(self) -> bool:
        return self.idx < len(self.nl)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())