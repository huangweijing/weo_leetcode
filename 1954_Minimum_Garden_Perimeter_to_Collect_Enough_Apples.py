class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        side_len = 0
        apples = 0
        while apples < neededApples:
            side_len += 1
            apples += 12 * side_len ** 2
        return side_len * 8
