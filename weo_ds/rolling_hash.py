
class Solution:
    # big prime number
    POW = 397
    # some big prime number
    MODULO = 100000000069

    @classmethod
    def hash(cls, nums: list[int]):
        hash_val = 0
        for num in nums:
            hash_val = (hash_val * Solution.POW + num) % Solution.MODULO
        return hash_val

    @classmethod
    def new_hash(cls, hash_val, k: int, prev_num, next_num):
        hash_val = (hash_val * Solution.POW + next_num) % Solution.MODULO
        hash_val = (hash_val - prev_num * (Solution.POW ** k)) % Solution.MODULO
        if hash_val < 0:
            hash_val += Solution.MODULO
        return hash_val