from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        # print(products)
        self.pre_table = dict[str, list[int]]()
        for idx, product in enumerate(products):
            for i in range(1, 1001):
                if i > len(product):
                    break
                key = product[:i]
                if key not in self.pre_table:
                    self.pre_table[key] = list[int]()
                if len(self.pre_table[key]) < 3:
                    self.pre_table[key].append(idx)
        # print(self.pre_table)

        result = list[list[str]]()
        for i in range(1, len(searchWord) + 1):
            key = searchWord[:i]
            # print(key)
            if key in self.pre_table.keys():
                word_idx_list = self.pre_table[key]
            else:
                word_idx_list = []
            word_list = []
            for word_idx in word_idx_list:
                word_list.append(products[word_idx])
            result.append(word_list)
        return result

sol = Solution()
r = sol.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "aa")
print(r)