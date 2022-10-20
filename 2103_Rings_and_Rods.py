class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = ord(rings[i + 1]) - ord("0")
            rods[rod].add(color)
        ans = 0
        for rod in rods:
            ans += 1 if len(rod) == 3 else 0
        return ans

