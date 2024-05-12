class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        calc_set = set[int]([x])
        tried_set = set[int]([x])
        op_cnt = 0
        while len(calc_set) > 0:
            if y in tried_set:
                return op_cnt
            new_calc_set = set[int]()
            while len(calc_set):
                val = calc_set.pop()
                if val % 5 == 0:
                    new_val = val // 5
                    if new_val not in tried_set:
                        tried_set.add(new_val)
                        new_calc_set.add(new_val)
                if val % 11 == 0:
                    new_val = val // 11
                    if new_val not in tried_set:
                        tried_set.add(new_val)
                        new_calc_set.add(new_val)
                if val + 1 <= 10000 and val + 1 not in tried_set:
                    tried_set.add(val + 1)
                    new_calc_set.add(val + 1)
                if val - 1 >= 0 and val - 1 not in tried_set:
                    tried_set.add(val - 1)
                    new_calc_set.add(val - 1)
            calc_set = new_calc_set
            op_cnt += 1


