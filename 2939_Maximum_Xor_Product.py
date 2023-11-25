class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        bin_a, bin_b = bin(a)[2:].rjust(50, "0"), bin(b)[2:].rjust(50, "0")
        v1, v2 = 0, 0
        for i in range(len(bin_a)):
            if i >= len(bin_a) - n:
                if bin_a[i] == bin_b[i]:
                    v1 += 1 << (len(bin_a) - 1 - i)
                    v2 += 1 << (len(bin_a) - 1 - i)
                else:
                    if v1 <= v2:
                        v1 += 1 << (len(bin_a) - 1 - i)
                    else:
                        v2 += 1 << (len(bin_b) - 1 - i)
            else:
                v1 += (0 if bin_a[i] == "0" else 1) << (len(bin_a) - 1 - i)
                v2 += (0 if bin_b[i] == "0" else 1) << (len(bin_b) - 1 - i)
            # print(bin(v1), bin(v2))
        return (v1 * v2) % (10 ** 9 + 7)

data = [
6
, 7
, 5
]
r = Solution().maximumXorProduct(*data)
print(r)