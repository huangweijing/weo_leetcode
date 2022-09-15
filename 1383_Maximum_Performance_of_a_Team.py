from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        if n == 1:
            return speed[0] * efficiency[0]

        eng_data = list(zip(speed, efficiency))
        eng_data.sort(key=lambda x: x[1], reverse=True)
        # print(eng_data)
        largest_k_heap = []
        result = eng_data[0][0] * eng_data[0][1]
        sum_speed = 0
        # result_arr = [result]
        for i in range(1, k):
            sum_speed += eng_data[i - 1][0]
            heapq.heappush(largest_k_heap, eng_data[i - 1][0])
            result = max((sum_speed + eng_data[i][0]) * eng_data[i][1], result)
            # result_arr.append((sum_speed + eng_data[i][0]) * eng_data[i][1])

        for i in range(k, n):
            # print(i, max_k_1_speed, result)
            heapq.heappush(largest_k_heap, eng_data[i - 1][0])
            popped_speed = heapq.heappop(largest_k_heap)
            sum_speed = sum_speed - popped_speed + eng_data[i - 1][0]
            # print(eng_data[i][0], sum_speed , eng_data[i][1])
            total_efficiency = (eng_data[i][0] + sum_speed) * eng_data[i][1]
            result = max(total_efficiency, result)
            # result_arr.append((eng_data[i][0] + sum_speed) * eng_data[i][1])
        # print(result_arr)
        return result % (10 ** 9 + 7)

data_speed = [4,4,10,5,5,5,10]
data_n = len(data_speed)
data_efficiency = [9,1,7,4,2,3,3]
data_k = 1

r = Solution().maxPerformance(data_n, data_speed, data_efficiency, data_k)
print(r)

# data = [3, 2, 4, 8, 5, 9, 1, 7]
# heapq.heapify(data)
# t = heapq.nlargest(100, data)
# print(t)