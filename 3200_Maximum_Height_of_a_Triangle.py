class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        max_height_red, max_height_blue = 0, 0
        red_cnt, blue_cnt = red, blue
        is_red = True
        while True:
            if is_red:
                if red_cnt >= max_height_red + 1:
                    max_height_red += 1
                    red_cnt -= max_height_red
                    is_red = False
                else:
                    break
            else:
                if blue_cnt >= max_height_red + 1:
                    max_height_red += 1
                    blue_cnt -= max_height_red
                    is_red = True
                else:
                    break
            # print(red_cnt, blue_cnt)
        # print("--")
        is_red = False
        red_cnt, blue_cnt = red, blue
        while True:
            if is_red:
                if red_cnt >= max_height_blue + 1:
                    max_height_blue += 1
                    red_cnt -= max_height_blue
                    is_red = False
                else:
                    break
            else:
                if blue_cnt >= max_height_blue + 1:
                    max_height_blue += 1
                    blue_cnt -= max_height_blue
                    is_red = True
                else:
                    break
            # print(red_cnt, blue_cnt)
        # print(max_height_blue, max_height_blue)
        return max(max_height_blue, max_height_red)


data = [2, 4]
r = Solution().maxHeightOfTriangle(* data)
print(r)
