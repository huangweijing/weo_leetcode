from typing import List

class Solution:
    def __init__(self) -> None:
        self.presum = [0]
        self.stones = []

    def sum_range(self, left: int, right: int) -> int:
        return self.presum[right + 1] - self.presum[left]

    def my_sol(self) -> int:
        dp = [[0] * len(self.stones) for _ in self.stones]
        for i in reversed(range(len(self.stones))):
            for j in range(i, len(self.stones)):
                if 0 <= i + 1 <= j:
                    dp[i][j] = max(dp[i][j], self.sum_range(i + 1, j) -dp[i + 1][j])
                if i <= j - 1:
                    dp[i][j] = max(dp[i][j], self.sum_range(i, j - 1) -dp[i][j - 1])
        return dp[0][len(self.stones) - 1]

    def stoneGameVII(self, stones: List[int]) -> int:
        self.stones = stones
        for stone in stones:
            self.presum.append(self.presum[-1] + stone)
        res = self.my_sol()
        return res
    
import time

# data = [3,1,4]
start = time.time()
data = [249,595,13,199,880,556,635,577,194,629,273,67,592,210,106,895,700,803,260,608,364,691,882,570,336,937,7,446,752,547,594,861,261,135,401,388,315,909,987,871,207,832,989,765,848,1,951,67,414,133,508,59,426,881,597,828,151,148,817,461,121,543,745,984,387,499,165,851,521,738,932,25,383,164,312,992,909,487,87,528,136,493,760,483,595,451,794,800,414,335,517,387,621,252,879,135,659,451,629,562,812,929,517,611,198,696,922,538,57,56,107,333,158,699,121,842,588,155,263,286,756,889,52,469,380,789,393,927,214,70,108,758,537,884,952,612,813,437,10,340,816,687,745,989,560,882,208,879,618,947,811,573,243,174,664,970,490,76,525,681,325,764,624,582,23,383,339,324,575,627,602,104,140,491,131,531,409,382,58,83,840,597,423,726,229,892,629,99,915,250,692,630,33,200,322,443,866,916,974,176,331,884,315,440,172,920,501,432,587,978,341,200,800,49,592,480,208,50,722,111,555,112,610,738,295,130,282,483,977,756,225,853,166,882,95,415,440,730,253,61,883,964,91,776,673,250,843,266,573,82,630,46,359,618,230,560,21,44,703,183,190,20,332,906,480,339,881,417,432,259,189,828,393,533,504,662,408,135,377,631,419,591,349,112,977,624,59,1000,278,492,881,671,471,80,749,379,327,403,715,679,889,185,474,168,979,285,747,960,173,449,723,77,179,59,700,430,215,805,756,492,618,89,750,226,484,404,159,794,595,715,436,184,926,888,55,212,1000,392,169,676,1,65,790,259,915,537,362,744,657,681,178,618,459,423,171,428,931,798,880,769,363,52,547,843,537,220,772,502,439,40,139,935,462,311,139,870,847,490,860,198,211,247,246,841,531,553,973,88,689,655,907,898,86,223,279,739,566,245,3,144,849,718,549,5,732,583,902,216,648,867,64,838,359,961,185,807,432,780,480,773,282,69,771,982,150,928,277,176,770,477,545,108,594,579,186,325,829,543,21,609,649,893,763,270,947,384,411,485,933,150,966,729,822,661,399,406,578,487,935,434,756,832,26,772,341,211,659,534,506,570,763,224,80,623,683,949,898,995,714,534,964,640,473,322,193,7,173,329,248,103,625,917,142,236,166,731,80,656,927,242,992,12,839,126,192,172,578,225,559,464,304,882,655,184,531,801,692,212,305,727,23,227,523,366,925,366,25,720,191,499,606,166,340,738,1,40,795,255,968,321,536,774,750,566,641,533,850,70,516,405,397,346,178,155,241,610,322,575,480,519,45,303,399,442,345,486,480,130,630,507,759,522,690,399,235,853,646,852,995,36,117,682,642,337,724,1,992,437,959,290,730,749,643,964,499,815,262,916,45,334,502,925,959,810,217,275,516,171,609,716,857,512,234,653,206,22,660,985,566,150,520,812,941,98,697,473,647,714,693,365,420,725,376,533,710,194,571,670,223,246,649,724,963,283,539,647,154,48,766,209,412,680,184,651,736,724,492,380,574,883,166,54,385,132,912,113,842,719,565,662,899,765,118,965,155,50,100,666,193,441,408,225,439,521,738,399,530,978,531,152,921,11,129,698,833,321,691,709,821,310,299,100,588,759,872,778,644,883,652,433,863,833,920,734,324,577,820,120,615,126,261,275,627,871,387,43,776,509,968,605,443,48,169,172,458,647,530,557,709,982,117,140,598,603,315,26,111,179,399,444,430,201,693,172,242,846,34,339,84,299,252,690,876,638,920,453,652,11,43,205,390,601,771,666,384,909,322,270,797,85,417,22,175,216,638,468,309,237,526,77,459,146,946,892,639,815,69,959,344,731,939,914,33,333,265,802,277,361,212,518,566,1000,994,506,624,248,384,207,199,327,572,316,861,691,309,514,140,34,37,756,95,153,138,677,489,709,858,227,386,35,272,627,995,157,845,953,670,272,936,807,521,327,379,360,971,983,73,707,614,923,667,966,501,80,227,894,221,214,76,572,159,932,470,704,361,372,96,285,912,848,570,329,808,378,993,504,620,450,237,539,240,258,665,91,454,515,323,19,808,493,799,760,694,57,702,674,348,331,528,737,13,183,465]
r = Solution().stoneGameVII(data)
print(r)
# d = [ [0
#     for i in range(1000)]
#         for j in range(1000)
# ]
print(time.time() - start)
        