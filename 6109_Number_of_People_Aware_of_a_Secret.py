class Solution:
    def __init__(self):
        self.sum_people = [-1] * 1001
        self.new_people = [-1] * 1001
        self.forget_people = [-1] * 1001

    def calc_new_people(self, k: int, delay: int, forget: int) -> int:
        if k - delay < 1:
            return 0
        if k - delay == 1:
            return 1
        if self.new_people[k] != -1:
            return self.new_people[k]
        forget_sum = 0
        i = k - delay + 1
        while i <= k:
            forget_sum += self.calc_forget_people(i, delay, forget)
            i += 1
        result = self.calc_sum_people(k - delay, delay, forget) - forget_sum
        self.new_people[k] = result
        return result

    def calc_forget_people(self, k: int, delay: int, forget: int) -> int:
        if k - forget < 1:
            return 0
        if k - forget == 1:
            return 1
        if self.forget_people[k] != -1:
            return self.forget_people[k]
        result = self.calc_new_people(k - forget, delay, forget)
        self.forget_people[k] = result
        return result

    def calc_sum_people(self, k:int, delay: int, forget: int) -> int:
        if k == 1:
            return 1
        if self.sum_people[k] != -1:
            return self.sum_people[k]
        result = self.calc_sum_people(k - 1, delay, forget) + \
               self.calc_new_people(k, delay, forget) - self.calc_forget_people(k, delay, forget)

        self.sum_people[k] = result
        return result


    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        for i in range(1, n):
            self.calc_sum_people(i, delay, forget)
        return self.calc_sum_people(n, delay, forget) % (10 ** 9 + 7)


# r = Solution().peopleAwareOfSecret(6, 2, 4)
r = Solution().peopleAwareOfSecret(1000, 2, 2)
# r = Solution().calc_new_people(6, 2, 4)
# r = Solution().calc_forget_people(5, 2, 4)
print(r)
