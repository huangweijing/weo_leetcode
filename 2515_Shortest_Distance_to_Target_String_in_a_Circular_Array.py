import math
from typing import List

class Solution:
    def closetTarget(self, words: List[str]
                     , target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        step1, step2 = math.inf, math.inf
        i = startIndex + 1
        for step in range(len(words)):
            word = words[(i + step) % len(words)]
            if word == target:
                step1 = step + 1
                break
        i = startIndex - 1
        for step in range(len(words)):
            word = words[(i - step + len(words)) % len(words)]
            if word == target:
                step2 = step + 1
                break
        ans = min(step1, step2)
        if ans == math.inf:
            ans = -1
        return ans

data = [
    ["pgmiltbptl", "jnkxwutznb", "bmeirwjars", "ugzyaufzzp", "pgmiltbptl", "sfhtxkmzwn", "pgmiltbptl", "pgmiltbptl",
     "onvmgvjhxa", "jyzdtwbwqp"]
    , "pgmiltbptl"
    , 4
]
r = Solution().closetTarget(* data)
print(r)