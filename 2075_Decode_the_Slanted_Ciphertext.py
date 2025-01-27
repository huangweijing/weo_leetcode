class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        ans_arr = [""] * (len(encodedText) - rows * (rows - 1))
        for i in range(cols):
            for j in range(rows):
                encoded_row_idx = j
                encoded_col_idx = i + j
                if encoded_col_idx >= cols:
                    break
                ans_arr.append(encodedText[encoded_row_idx * cols + encoded_col_idx])

        return "".join(ans_arr).rstrip()
    

data = [
    "iveo    eed   l te   olc"
    , 4
]
r = Solution().decodeCiphertext(*data)
print(r)