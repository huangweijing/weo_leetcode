from functools import cache

class Solution:
    def __init__(self):
        self.result = set[int]()

    @cache
    def my_num_tile(self, titles: str) -> set[str]:
        if len(titles) == 1:
            return set(titles)
        ch = titles[0]
        sub_result = self.my_num_tile(titles[1:])
        result = sub_result.copy()
        result.add(ch)
        for sub in sub_result:
            for i in range(len(sub) + 1):
                # print(sub[:i], ch, sub[i:])
                result.add(sub[:i] + ch + sub[i:])
        # print(result)
        return result

    def numTilePossibilities(self, tiles: str) -> int:
        result = self.my_num_tile(tiles)
        # print(result)
        return len(result)

r = Solution().numTilePossibilities("AAABBCD")
print(r)