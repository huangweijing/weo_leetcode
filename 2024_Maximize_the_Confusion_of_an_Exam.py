class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left_pt, right_pt = 0, 0
        changed_cnt = 0
        ans = 0
        while not (right_pt == len(answerKey) and changed_cnt <= k):
            # print(answerKey, answerKey[left_pt], answerKey[right_pt], left_pt, right_pt)
            while right_pt < len(answerKey) and changed_cnt <= k:
                if answerKey[right_pt] == "F":
                    changed_cnt += 1
                if changed_cnt <= k:
                    ans = max(ans, right_pt - left_pt + 1)
                right_pt += 1

            while left_pt < len(answerKey) and changed_cnt > k:
                if answerKey[left_pt] == "F":
                    changed_cnt -= 1
                left_pt += 1


        left_pt, right_pt = 0, 0
        changed_cnt = 0
        while not (right_pt == len(answerKey) and changed_cnt <= k):
            # print(answerKey, answerKey[left_pt], answerKey[right_pt], left_pt, right_pt)
            while right_pt < len(answerKey) and changed_cnt <= k:
                if answerKey[right_pt] == "T":
                    changed_cnt += 1
                if changed_cnt <= k:
                    ans = max(ans, right_pt - left_pt + 1)
                right_pt += 1

            while left_pt < len(answerKey) and changed_cnt > k:
                if answerKey[left_pt] == "T":
                    changed_cnt -= 1
                left_pt += 1

        return ans


data = [
    "TTFTTFTTTTTTFTT"
    , 3
]
r = Solution().maxConsecutiveAnswers(* data)
print(r)

