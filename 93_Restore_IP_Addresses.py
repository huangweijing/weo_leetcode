from typing import List

class Solution:
    def my_restore_ip(self, s:str, sec_cnt: int) -> List[str]:
        if sec_cnt > 4:
            return []
        if sec_cnt == 4:
            if s == "" or int(s) > 255 or (s[0] == "0" and len(s) > 1):
                return []
            else:
                return [s]

        result = []
        for i in range(3):
            sec = s[:i + 1]
            if sec == "" or int(sec) > 255 or (sec[0] == "0" and len(sec) > 1):
                continue
            ip_list_n_1 = self.my_restore_ip(s[i + 1: ], sec_cnt + 1)
            for ip in ip_list_n_1:
                result.append(f"{sec}.{ip}")

        return result

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.my_restore_ip(s, 1)

r = Solution().restoreIpAddresses("101023")
print(r)
