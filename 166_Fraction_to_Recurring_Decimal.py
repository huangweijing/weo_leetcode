from collections import deque


class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = numerator // abs(numerator)
        sign *= denominator // abs(denominator)
        sign_char = "" if sign == 1 else "-"
        numerator, denominator = abs(numerator), abs(denominator)
        num = deque(str(numerator))
        remainder = 0
        ans = []
        rem_dict = dict[int, int]()
        int_len = len(str(numerator))
        while not (len(num) == 0 and remainder == 0):
            # print(len(num), remainder, len(rem_set))
            while (remainder == 0 and len(num) > 0) or\
                    (remainder != 0 and remainder < denominator):
                if len(num) == 0:
                    remainder *= 10
                else:
                    remainder = remainder * 10 + int(num.popleft())
                if len(ans) >= int_len:
                    # print(ans)
                    if remainder in rem_dict:
                        loop_len = len(ans) - rem_dict[remainder]
                        int_part = str(int("".join(map(str, ans[:int_len]))))
                        float_no_loop_part = ("".join(map(str, ans[int_len: -loop_len])))
                        float_loop_part = "".join(map(str, ans[-loop_len:]))
                        return f"{sign_char}{int_part}.{float_no_loop_part}({float_loop_part})"
                    else:
                        rem_dict[remainder] = len(ans)
                ans.append(0)

            ans[-1] = remainder // denominator
            remainder = remainder % denominator
        # print(ans[:int_len], )
        int_part = str(int("".join(map(str, ans[:int_len]))))
        float_no_loop_part = ("".join(map(str, ans[int_len: ])))
        if len(float_no_loop_part) == 0:
            return f"{sign_char}{int_part}"
        else:
            return f"{sign_char}{int_part}.{float_no_loop_part}"


r = Solution().fractionToDecimal(1, 12345)
print(r)
# num, dsr = 1, 72
# e = 0
# ans = ""
# while num != 0:
#     e, div, rem = Solution().divide(e, num, dsr)
#     ans += str(div).rjust(e, "0")
#     print(ans)


