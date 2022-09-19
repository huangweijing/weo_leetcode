class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num_str = ""
        result = set[int]()
        for ch in word:
            if "0" <= ch <= "9":
                num_str += ch
            else:
                if len(num_str) > 0:
                    result.add(int(num_str))
                num_str = ""

        if len(num_str) > 0:
            result.add(int(num_str))

        return len(result)
