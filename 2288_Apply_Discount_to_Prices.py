import re


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        arr = sentence.split(sep=" ")
        pat = re.compile("^\\$(\\d+)$")
        ans = []
        for word in arr:
            matches = pat.match(word)
            if matches:
                new_price = int(matches.group(1)) * (100 - discount) / 100
                new_word = f"${new_price:.2f}"
                ans.append(new_word)
            else:
                ans.append(word)
        return " ".join(ans)


data = [
    "there are $1 $2 and 5$ candies in the shop"
    , 50
]
r = Solution().discountPrices(*data)
print(r)

