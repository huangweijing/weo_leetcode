from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            arr = log.split(" ")
            # print(arr)
            if "0" <= arr[1][0] <= "9":
                digit_logs.append(log)
            else:
                letter_logs.append([" ".join(arr[1:]), arr[0], log])
        letter_logs.sort()
        letter_logs = [log[2] for log in letter_logs]
        ans = []
        ans.extend(letter_logs)
        ans.extend(digit_logs)
        return ans

data = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
r = Solution().reorderLogFiles(data)
print(r)