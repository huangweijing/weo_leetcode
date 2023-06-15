from typing import List
from sortedcontainers import SortedList



class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        num_list = list(zip(nums1, nums2))
        # num_list.sort(key=lambda )
        sl1 = SortedList(zip(nums1[: k], nums2[: k]), key=lambda x: (x[0], x[1]))
        sl2 = SortedList(zip(nums1[: k], nums2[: k]), key=lambda x: (x[1], x[0]))
        sum_num1 = sum(nums1[: k])
        min_num2 = min(nums2[: k])
        ans = sum_num1 * min_num2
        for i in range(k, len(nums1)):
            sl1.add((nums1[i], nums2[i]))
            sl2.add((nums1[i], nums2[i]))
            sum_num1 += nums1[i]

            #sol1
            if sl2[0][1] == sl1[0][1]:
                # sl1中最小的元素，他的pair正好在sl2中也最小
                max1 = (sum_num1 - sl1[0][0]) * sl2[1][1]
            else:
                # sl1中最小的元素，他的pair正好在sl2中非最小
                max1 = (sum_num1 - sl1[0][0]) * sl2[0][1]

            # 取sl2中最小的元素进行计算
            max2 = (sum_num1 - sl2[0][0]) * sl2[1][1]
            ans = max(ans, max1, max2)
            if max1 > max2:
                to_remove = sl1[0]
                sum_num1 -= to_remove[0]
                sl1.remove(to_remove)
                sl2.remove(to_remove)
            else:
                to_remove = sl2[0]
                sum_num1 -= to_remove[0]
                sl2.remove(to_remove)
                sl1.remove(to_remove)

            print(sl1)
            print(sl2)
            print()

        return ans




data = [
    [93, 463, 179, 2488, 619, 2006, 1561, 137, 53, 1765, 2304, 1459, 1768, 450, 1938, 2054, 466, 331, 670, 1830, 1550,
     1534, 2164, 1280, 2277, 2312, 1509, 867, 2223, 1482, 2379, 1032, 359, 1746, 966, 232, 67, 1203, 2474, 944, 1740,
     1775, 1799, 1156, 1982, 1416, 511, 1167, 1334, 2344]
    , [345, 229, 976, 2086, 567, 726, 1640, 2451, 1829, 77, 1631, 306, 2032, 2497, 551, 2005, 2009, 1855, 1685, 729, 2498, 2204, 588, 474, 693, 30, 2051, 1126, 1293, 1378, 1693, 1995, 2188, 1284, 1414, 1618, 2005, 1005, 1890, 30, 895, 155, 526, 682, 2454, 278, 999, 1417, 1682, 995]
    , 42
]
r = Solution().maxScore(* data)
print(r)

sl = SortedList([[1, 2], [3, 4]])
