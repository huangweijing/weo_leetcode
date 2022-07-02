from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        text = list[str]()
        idx = 0
        while idx < len(words):
            new_idx = idx
            words_len = 0
            words_len_sum = 0
            word_line = []
            line = ""
            while new_idx < len(words):
                if new_idx != idx:
                    words_len += 1
                if words_len + len(words[new_idx]) > maxWidth:
                    break
                words_len += len(words[new_idx])
                words_len_sum += len(words[new_idx])
                word_line.append(words[new_idx])
                new_idx += 1

            if len(word_line) == 1 or new_idx == len(words):
                line = " ".join(word_line)
                line += " " * (maxWidth - len(line))
            else:
                span_count = len(word_line) - 1
                interval_space = int((maxWidth - words_len_sum)/ span_count)
                remainder_space = (maxWidth - words_len_sum) % span_count
                # print(word_line)
                for word_idx in range(len(word_line)):
                    if word_idx == len(word_line) - 1:
                        line = line + word_line[word_idx]
                        continue
                    line = line + word_line[word_idx]
                    line = line + " " * interval_space
                    if remainder_space > 0:
                        line = line + " "
                        remainder_space -= 1

            text.append(line)
            idx = new_idx

        return text



sol = Solution()
r = sol.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
print(r)

