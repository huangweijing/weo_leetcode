from typing import List
from collections import defaultdict
from sortedcontainers import SortedList


class Food:
    def __init__(self, name: str, cuisine: str, rating: int):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating

    def __lt__(self, other):
        if self.rating < other.rating:
            return True
        if self.rating == other.rating:
            return self.name > other.name
        return False

    def __str__(self):
        return f"<{self.name}-{self.cuisine}: {self.rating}>"

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_dict = dict[str, Food]()
        self.cuisine_dict = defaultdict(lambda : SortedList())
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            f = Food(food, cuisine, rating)
            self.food_dict[food] = f
            self.cuisine_dict[cuisine].add(f)

    def changeRating(self, food: str, newRating: int) -> None:
        f = self.food_dict[food]
        sl = self.cuisine_dict[f.cuisine]
        sl.remove(f)
        f.rating = newRating
        sl.add(f)

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_dict[cuisine][-1].name

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
data = [
    ["FoodRatings","highestRated","highestRated","changeRating","highestRated","changeRating","highestRated"]
    , [[["kimchi","miso","sushi","moussaka","ramen","bulgogi"],["korean","japanese","japanese","greek","japanese","korean"],[9,12,8,15,14,7]],["korean"],["japanese"],["sushi",16],["japanese"],["ramen",16],["japanese"]]
]
ssa = FoodRatings(*data[1][0])
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret)
    result.append(ret)
print(result)
print(list(map(str, ssa.cuisine_dict['japanese'])))