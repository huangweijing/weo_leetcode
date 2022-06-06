class Solution:
    def countLatticePoints(self, circles: list) -> int:
        x = 0
        result = 0

        border_x = 0
        border_y = 0

        for circle in circles:
            xr = circle[0] + circle[2]
            yr = circle[1] + circle[2]
            if border_x < xr:
                border_x = xr
            if border_y < yr:
                border_y = yr

        while x <= border_x:
            y = 0
            while y <= border_y:
                for circle in circles:
                    # abs(circle[0] - x) * 3.14 < circle[2] / 3.1415
                    if pow((circle[0] - x), 2) + pow((circle[1] - y), 2) <= pow(circle[2], 2):
                        result = result + 1
                        break
                y = y + 1
            x = x + 1
        return result

sol = Solution()
r = sol.countLatticePoints([[5,9,5],[7,6,1],[10,5,2],[3,8,2],[2,4,2],[8,8,1],[4,7,3],[6,4,4],[4,3,1],[9,7,6],[1,6,1],[7,7,3],[7,3,3]])
print(r)
