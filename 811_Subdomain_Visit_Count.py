from typing import List
from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_cnt = Counter()
        for domains in cpdomains:
            arr = domains.split(" ")
            cnt = int(arr[0])
            domain_str = arr[1]
            domain_str_split = domain_str.split(".")
            for i, domain in enumerate(domain_str_split):
                # if i == 0:
                #     continue
                d = ".".join(domain_str_split[i:])
                domain_cnt[d] += cnt
        return [f"{val} {key}" for key, val in domain_cnt.items()]



