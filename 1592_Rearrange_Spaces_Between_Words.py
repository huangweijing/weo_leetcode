class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_cnt = 0
        for ch in text:
            if ch == " ":
                space_cnt += 1
        text_arr = text.split(sep=" ")
        text_arr = list(filter(lambda x: x != "", text_arr))
        if len(text_arr) <= 1:
            return "".join(text_arr) + " " * space_cnt
        return (" " * (space_cnt // (len(text_arr) - 1))).join(text_arr) + \
            " " * (space_cnt % (len(text_arr) - 1))