import math
import bisect


def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return ([2] if n > 2 else []) + [i for i in range(3, n, 2) if sieve[i]]


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        ls, rs = math.sqrt(l), math.sqrt(r)
        if ls > int(ls):
            ls = int(ls) + 1
        else:
            ls = int(ls)
        rs = int(rs)
        primes = rwh_primes(rs + 1)
        pl = bisect.bisect_right(primes, ls)
        if pl > 0 and primes[pl - 1] == ls:
            pl -= 1
        return r - l + 1 - (len(primes) - pl)


res = Solution().nonSpecialCount(1, 2)
print(res)
