class Solution:
    num_word = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"         
    }

    def numUnder100(self, num: int) -> str:
        if num <= 20:
            return self.num_word[num]
        elif num % 10 == 0:
            return self.num_word[num // 10 * 10]
        return self.num_word[num // 10 * 10] + " " + self.numUnder100(num % 10)
        
    def numUnder1000(self, num: int) -> str:
        if num < 100:
            return self.numUnder100(num)
        elif num % 100 == 0:
            return self.numUnder100(num // 100) + " " + self.num_word[100]
        return self.numUnder100(num // 100) + " " + self.num_word[100] + " " + self.numUnder100(num % 100)


    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.num_word[num]
        ans = ""
        for i in [1000000000, 1000000, 1000]:
            if num // i > 0:
                ans += " " + self.numUnder1000(num // i) + " " + self.num_word[i]
                # print(i, ans, num)
                num %= i
        if num > 0:
            ans += " " + self.numUnder1000(num)
        return ans.strip()

s = Solution()
r = Solution().numberToWords(2147483648)
print(r)
print(s.numUnder100(22))