from functools import cache
from collections import Counter


class Solution:
    def __init__(self) -> None:
        self.s = ""
        self.jump_point = []
        
    @cache
    def my_sol(self, idx: int) -> int:
        # print(f"in method, {idx}")
        if idx == len(self.s) - 1:
            return 1
        ans = len(self.s) - idx
        for jp in self.jump_point[idx]:
            ans = min(ans, 1 + self.my_sol(jp + 1))
        # print(idx, ans)
        return ans

    def minimumSubstringsInPartition(self, s: str) -> int:
        self.s = s
        self.jump_point = [set() for _ in range(len(s) + 1)]
        # print(self.cnt_arr)
        # print(time.time() - t1)
        for i in range(len(s)):
            cnt = Counter()
            for j in range(i, len(s)):
                cnt[s[j]] += 1
                # print(cnt)
                if len(set(cnt.values())) == 1:
                    self.jump_point[i].add(j)
        # print(time.time() - t1)
        ans = self.my_sol(0)
        return ans
    
import logging
import time
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(level=logging.INFO)
t1 = time.time()
logging.info("start")
data = "xxaqymovnvxilbabqqjkkixxeyyibeewwjiyyjjscllmlbewptegeebaffhuhhhuuupopoyyvqpqyybbcmkkhvwlbolklrkfffqpputtwrqqmhggfsbbllsxnzzzzpppuvmwmwkusaalvsffzesfegjfncdaadurjmjmannsjmxvorsssdvvxyxfbnxrgghgfdddppvrrurlllopmoojsccededdoppocellcuvoengerfejjijllqqqqktgkghhqmmsssxxtucooxozzzrdswwijtzzhumbqqromggirrddqudbdsqmkztxxyggggdbdufnvsswotvvuuvveeoyddsdegsqppahbctvhucccdsnmnyyjjjklssqwbvveurpfddpppvjjggggcwemmupfgeffftttfsefwiigmnmvwxxykkkfllllwadeebnnrtogrwzdwwwpllhhcbjiiioonywwhhkkkhhonuuwwyvwwnmmyyydddgqkkkxxxxwqezyzllmwwxtppwxutuvcccctfllrnnzsfcvvvvfkrzvvxpojjmavmmaarqaqeelrwwziqpnpoplgssvvvnvffffrkxedffbtzzztbddrkkzxyeefvvoimxeddghdhvbtggqjxltggllllyzjcssvvvttttxyywgwqqqcrrtbmlmeewwvcttonkfddnsiagzuwgliaspqjkgoooudlmskzzzcmxmocnwtgggyhuuuubtttuurrddijellxaaahhhyybayhhhjrxwppdmmooovuqoooaayheejjjqqooayfzrxistzavqqqqluwvolkvhrsqybkljjjjjvjdkzsxxbggmmijiuitstckiivqcczlmtxxxoollhlccitasobcygjiiaazeyykhfggfctthhddlbttjhjkhkjqmnihjgttwsenssszfihhqaggeedqqpsdcttttttnninnggguushhhhhheggssnaatrzvwxu"
r = Solution().minimumSubstringsInPartition(data)
logging.info(r)
t2 = time.time()
logging.info(t2 - t1)
logging.info("end")