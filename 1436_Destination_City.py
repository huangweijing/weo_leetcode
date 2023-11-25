class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src_cities, dest_cities = set[str](), set[str]()
        for path in paths:
            src_cities.add(path[0])
            dest_cities.add(path[1])
        for city in src_cities:
            if city in dest_cities:
                dest_cities.remove(city)
        return dest_cities.pop()


