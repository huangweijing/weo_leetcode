class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        sec_dict = dict[str, int]()
        gue_dict = dict[str, int]()
        for i, ch in enumerate(secret):
            if guess[i] == ch:
                a += 1
                continue
            if ch not in sec_dict:
                sec_dict[ch] = 0
            if guess[i] not in gue_dict:
                gue_dict[guess[i]] = 0
            sec_dict[ch] += 1
            gue_dict[guess[i]] += 1

        for key in gue_dict.keys():
            gcnt = gue_dict[key]
            if key in sec_dict:
                scnt = sec_dict[key]
            else:
                scnt = 0
            b += min(gcnt, scnt)

        return f"{a}A{b}B"