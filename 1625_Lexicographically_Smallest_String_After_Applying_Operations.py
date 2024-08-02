from collections import deque


class Solution:
    def min_num(self, num: int, a: int) -> list[int]:
        ret = [num, 0]
        cur = num
        dup_set = set[int]()
        cnt = 0
        while cur not in dup_set:
            dup_set.add(cur)
            if cur < ret[0]:
                ret = [cur, cnt]
            cur = (cur + a) % 10
            cnt += 1
        return ret
    
    def shift_right(self, s: deque, b: int) -> deque:
        while b > 0:
            s.append(s.popleft())
            b -= 1
        return s
    
    def shift_smallest_even(self, s: deque, a: int):
        mn = self.min_num(s[0], a)
        for i in range(len(s)):
            if i & 1 == 0:
                s[i] = (s[i] + mn[1] * a) % 10

    
    def shift_smallest_odd(self, s: deque, a: int):
        if len(s) <= 1:
            return
        mn = self.min_num(s[1], a)
        for i in range(len(s)):
            if i & 1 == 1:
                s[i] = (s[i] + mn[1] * a) % 10

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        shift_set = set[int]()
        shift = 0
        smallest = deque([ 99 ])
        sq = deque(map(lambda num_str: int(num_str) ,s))
        can_even_shift = False
        while shift not in shift_set:
            shift_set.add(shift)
            if shift & 1 == 1:
                can_even_shift = True
            shift = (shift + b) % len(s)
        # print(shift_set)
        for shift in shift_set:
            sq = deque(map(lambda num_str: int(num_str) ,s))
            sq = self.shift_right(sq, shift)
            # print(sq)
            self.shift_smallest_odd(sq, a)
            # print(sq)
            if can_even_shift:
                self.shift_smallest_even(sq, a)
            # print(sq)
            if sq < smallest:
                smallest = sq
            # print("-----")

        ans = "".join(map(lambda num: str(num) ,smallest))
        return ans
    
data = [
    "565510"
    , 7
    , 2
]
r = Solution().findLexSmallestString(* data)
print(r)
        