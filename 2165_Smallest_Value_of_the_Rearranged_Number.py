class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        sign = num // abs(num)
        num = abs(num)
        if sign > 0:
            num_arr = list(sorted(str(num)))
            for i in range(len(num_arr)):
                if num_arr[i] != "0":
                    num_arr[0], num_arr[i] = num_arr[i], num_arr[0]
                    return int("".join(num_arr)) * sign
        else:
            num_arr = list(reversed(sorted(str(num))))
            return int("".join(num_arr)) * sign
        return -1

