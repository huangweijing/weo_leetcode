from typing import List


class WeightedUnionFind:

    def __init__(self, size):
        self.node = [i for i in range(size)]
        self.size = [1] * size
        self.count = size
        pass

    def find(self, p: int):
        while self.node[p] != p:
            p = self.node[p]
        return p


    def union_all(self, arr: list[int]):
        if len(arr) == 1:
            return
        for e in arr[1:]:
            self.union(arr[0], e)


    def union(self, p: int, q: int):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return
        if self.size[p] < self.size[q]:
            self.node[p] = q
            self.size[q] = self.size[q] + self.size[p]
        else:
            self.node[q] = p
            self.size[p] = self.size[q] + self.size[p]
        self.count -= 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_id_dict = dict[str, int]()
        id_email_dict = dict[int, str]()
        email_name_dict = dict[str, str]()
        for account in accounts:
            for email in account[1:]:
                if email in email_id_dict:
                    continue
                email_name_dict[email] = account[0]
                email_id_dict[email] = len(email_id_dict)
                id_email_dict[email_id_dict[email]] = email
        wuf = WeightedUnionFind(len(email_id_dict))
        for account in accounts:
            wuf.union_all(list(map(email_id_dict.get, account[1:])))
        ans_dict = dict[int, list[str]]()
        for email, email_id in email_id_dict.items():
            group_id = wuf.find(email_id)
            name = email_name_dict[email]
            if group_id not in ans_dict:
                ans_dict[group_id] = [name]
            ans_dict[group_id].append(email)
        ans = []
        for item in ans_dict.values():
            arr = [item[0]]
            email_list = list(item[1:])
            email_list.sort()
            arr.extend(email_list)
            ans.append(arr)

        return ans

data = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"]
    ,["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"]
    ,["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"]
    ,["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"]
    ,["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
r = Solution().accountsMerge(data)
print(r)
