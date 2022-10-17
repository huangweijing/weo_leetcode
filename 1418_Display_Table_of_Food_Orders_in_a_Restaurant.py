from typing import List
from sortedcontainers import SortedSet, SortedDict
from collections import Counter

class Table:
    def __init__(self, table_no: int, food: str):
        self.food = Counter()
        self.table_no = table_no
        self.take_order(food)

    def take_order(self, food: str):
        self.food[food] += 1

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_dict = SortedDict()
        food_set = SortedSet()
        for order in orders:
            table_no = int(order[1])
            food_set.add(order[2])
            if table_no not in table_dict:
                table_dict[table_no] = Table(table_no, order[2])
            else:
                table_dict[table_no].take_order(order[2])
        display_table = list[list[str]]()
        title = ["Table"]
        title.extend(food_set)
        display_table.append(title)
        for key, item in table_dict.items():
            row = list[str]()
            row.append(str(key)) #table no
            for f in food_set:
                row.append(str(item.food[f]))
            display_table.append(row)
        return display_table

data_orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
r = Solution().displayTable(data_orders)
print(r)

