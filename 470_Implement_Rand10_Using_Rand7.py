# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

def rand7():
    pass

class Solution:
    def rand10(self) -> int:
        rand_sum = 0
        for rand in range(10):
            rand_sum += rand7()
        return rand_sum % 10 + 1
