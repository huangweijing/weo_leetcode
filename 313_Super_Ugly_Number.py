from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        super_ugly_number = [1]
        un_set = set[int]()
        t = 0
        while t < n:
            un = heapq.heappop(super_ugly_number)
            if un not in un_set:
                un_set.add(un)
                t += 1
                if t == n:
                    return un
                for prime in primes:
                    heapq.heappush(super_ugly_number, un * prime)

data_n = 100000
data_prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541]
r = Solution().nthSuperUglyNumber(data_n, data_prime)
print(r)

