class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_dict = dict[int, int]()
        ans = len(cards) + 1
        for i, card in enumerate(cards):
            if card in card_dict:
                ans = min(ans, i - card_dict[card] + 1)
            card_dict[card] = i
        if ans == len(cards) + 1:
            ans = -1
        return ans
