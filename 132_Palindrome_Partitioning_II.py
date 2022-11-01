import datetime
from functools import cache
from collections import Counter

class Solution:
    def __init__(self):
        self.s = ""
        self.cnt = Counter()
        # self.acc_counter = []

    # def acc_cnt(self):
    #     for i in range(len(self.s)):
    #         self.acc_counter.append(Counter(self.s[:i + 1]))

    @cache
    def is_palindrome(self, s: str) -> bool:
        self.cnt[0] += 1
        if s[0] == s[-1]:
            if len(s) > 3:
                return self.is_palindrome(s[1:-1])
            else:
                return True
        return False

    @cache
    def is_palindrome_idx(self, sta: int, end: int) -> bool:
        self.cnt[0] += 1
        if self.s[sta] == self.s[end]:
            if end - sta + 1 > 3:
                return self.is_palindrome_idx(sta + 1, end - 1)
            else:
                return True
        return False



    @cache
    def my_cut(self, start_idx: int) -> int:
        if start_idx == len(self.s):
            return 0
        # if self.is_palindrome(self.s[start_idx: ]):
        if self.is_palindrome_idx(start_idx, len(self.s) - 1):
            return 1

        ans = len(self.s) - start_idx
        for cut in range(start_idx, len(self.s)):
            # if self.is_palindrome(self.s[start_idx: cut + 1])::
            if self.is_palindrome_idx(start_idx, cut):
                self.cnt[1] += 1
                sub_cut = self.my_cut(cut + 1) + 1
                ans = min(ans, sub_cut)
                if ans == 2:
                    break
        return ans

    def minCut(self, s: str) -> int:
        self.s = s
        # self.acc_cnt()
        for i in range(len(self.s) - 1, -1, -1500):
            self.my_cut(i)
        return self.my_cut(0) - 1

# print(Solution().is_palindrome("aabaa"))
import  sys
sys.setrecursionlimit(30000)
t1 = datetime.datetime.now()

sol = Solution()
r = sol.minCut("fiefhgdcdcgfeibggchibffahiededbbegegdfibdbfdadfbdbceaadeceeefiheibahgececggaehbdcgebaigfacifhdbecbebfhiefchaaheiichgdbheacfbhfiaffaecicbegdgeiaiccghggdfggbebdaefcagihbdhhigdgbghbahhhdagbdaefeccfiaifffcfehfcdiiieibadcedibbedgfegibefagfccahfcbegdfdhhdgfhgbchiaieehdgdabhidhfeecgfiibediiafacagigbhchcdhbaigdcedggehhgdhedaebchcafcdehcffdiagcafcgiidhdhedgaaegdchibhdaegdfdaiiidcihifbfidechicighbcbgibadbabieaafgeagfhebfaheaeeibagdfhadifafghbfihehgcgggffgbfccgafigieadfehieafaehaggeeaaaehggffccddchibegfhdfafhadgeieggiigacbfgcagigbhbhefcadafhafdiegahbhccidbeeagcgebehheebfaechceefdiafgeddhdfcadfdafbhiifigcbddahbabbeedidhaieagheihhgffbfbiacgdaifbedaegbhigghfeiahcdieghhdabdggfcgbafgibiifdeefcbegcfcdihaeacihgdchihdadifeifdgecbchgdgdcifedacfddhhbcagaicbebbiadgbddcbagbafeadhddaeebdgdebafabghcabdhdgieiahggddigefddccfccibifgbfcdccghgceigdfdbghdihechfabhbacifgbiiiihcgifhdbhfcaiefhccibebcahidachfabicbdabibiachahggffiibbgchbidfbbhfcicfafgcagaaadbacddfiigdiiffhbbehaaacidggfbhgeaghigihggfcdcidbfccahhgaffiibbhidhdacacdfebedbiacaidaachegffaiiegeabfdgdcgdacfcfhdcbfiaaifgfaciacfghagceaaebhhibbieehhcbiggabefbeigcbhbcidbfhfcgdddgdffghidbbbfbdhcgabaagddcebaechbbiegeiggbabdhgghciheabdibefdfghbfbfebidhicdhbeghebeddgfdfhefebiiebdchifbcbahaddhbfafbbcebiigadhgcfbebgbebhfddgdeehhgdegaeedfadegfeihcgeefbbagbbacbgggciehdhiggcgaaicceeaefgcehfhfdciaghcbbgdihbhecfbgffefhgiefgeiggcebgaacefidghdfdhiabgibchdicdehahbibeddegfciaeaffgbefbbeihbafbagagedgbdadfdggfeaebaidchgdbcifhahgfdcehbahhdggcdggceiabhhafghegfdiegbcadgaecdcdddfhicabdfhbdiiceiegiedecdifhbhhfhgdbhibbdgafhgdcheefdhifgddchadbdggiidhbhegbdfdidhhfbehibiaacdfbiagcbheabaaebfeaeafbgigiefeaeheabifgcfibiddadicheahgbfhbhddaheghddceedigddhchecaghdegigbegcbfgbggdgbbigegffhcfcbbebdchffhddbfhhfgegggibhafiebcfgeaeehgdgbccbfghagfdbdfcbcigbigaccecfehcffahiafgabfcaefbghccieehhhiighcfeabffggfchfdgcfhadgidabdceediefdccceidcfbfiiaidechhbhdccccaigeegcaicabbifigcghcefaafaefd")
print(sol.cnt)
print(r)

t2 = datetime.datetime.now()
print(t2 - t1)

