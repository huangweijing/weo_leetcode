class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        consecution_cnt = 0
        for num in nums:
            if num == 1:
                consecution_cnt += 1
                if consecution_cnt > result:
                    result = consecution_cnt
            else:
                consecution_cnt = 0
        return result
