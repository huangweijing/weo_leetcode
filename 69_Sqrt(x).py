class Solution:
    def mySqrt(self, x: int) -> int:
        left_wall = 0
        right_wall = x
        result = (left_wall + right_wall + 1) >> 1
        cnt = 0
        while left_wall < right_wall:
            # print(result)
            cnt += 1
            result_2 = result ** 2
            result_1_2 = (result + 1) ** 2
            if result_2 <= x < result_1_2:
                # print(cnt)
                return result
            elif result_2 > x:
                right_wall = result
                result = (left_wall + right_wall + 1) >> 1
            elif result_1_2 <= x:
                left_wall = result
                result = (left_wall + right_wall + 1) >> 1
        return result

sol = Solution()
r = sol.mySqrt(36)
print(r)