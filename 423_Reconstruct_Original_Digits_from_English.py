from collections import Counter


class Solution:
    def str2num(self, cnt: Counter, word: str, rep: str) -> int:
        ret = cnt[rep]
        for ch in word:
            cnt[ch] -= ret
        return ret
        
    def originalDigits(self, s: str) -> str:
        ch_cnt = [0] * 10
        cnt = Counter(s)
        ch_cnt[0] = self.str2num(cnt=cnt, word="zero", rep="z")
        ch_cnt[2] = self.str2num(cnt=cnt, word="two", rep="w")
        ch_cnt[6] = self.str2num(cnt=cnt, word="six", rep="x")
        ch_cnt[8] = self.str2num(cnt=cnt, word="eight", rep="g")
        ch_cnt[7] = self.str2num(cnt=cnt, word="seven", rep="s")
        ch_cnt[3] = self.str2num(cnt=cnt, word="three", rep="h")
        ch_cnt[5] = self.str2num(cnt=cnt, word="five", rep="v")
        ch_cnt[4] = self.str2num(cnt=cnt, word="four", rep="f")
        ch_cnt[1] = self.str2num(cnt=cnt, word="one", rep="o")
        ch_cnt[9] = self.str2num(cnt=cnt, word="nine", rep="i")
        return "".join(str(i) * val for i, val in enumerate(ch_cnt))
            
r = Solution().originalDigits("owoztneoer")
print(r)
        