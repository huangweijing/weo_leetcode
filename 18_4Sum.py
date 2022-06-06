class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        result_set = set()
        input_hash = dict()
        num_arr = dict()
        new_num = 1
        for num in nums:
            if num not in num_arr:
                num_arr[num] = 0
            num_arr[num] += 1
            input_hash[num] = new_num
            new_num += 1
        len_num = len(nums)
        for i in range(len_num):
            for j in range(i+1, len_num):
                for k in range(j+1, len_num):
                    d = target - nums[i] - nums[j] - nums[k]
                    if d < nums[k]:
                        continue
                    # print(nums, nums[i], nums[j], nums[k], d)
                    if d not in num_arr:
                        continue
                    threshold = 1
                    if nums[i] == d:
                        threshold += 1
                    if nums[j] == d:
                        threshold += 1
                    if nums[k] == d:
                        threshold += 1
                    # print(f"threshold={threshold}, num_arr[d]={num_arr[d]}")
                    if num_arr[d] >= threshold:
                        hash_value = input_hash[nums[i]] * (200 ** 3) + \
                                     input_hash[nums[j]] * (200 ** 2) + \
                                     input_hash[nums[k]] * 200 + \
                                     input_hash[d]
                        # print(f"hash_value={hash_value}")
                        if hash_value not in result_set:
                            # print(f"new result={[nums[i], nums[j], nums[k], d]}")
                            result.append([nums[i], nums[j], nums[k], d])
                            result_set.add(hash_value)

        # print(f"input_hash={input_hash}")
        # print(f"list(result_set)={list(result_set)}")
        # print(f"num_arr={num_arr}")
        return result


sol = Solution()
r = sol.fourSum([2,0,3,0,1,2,4], 7)
print(r)
