import datetime


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str
                          , arriveBob: str, leaveBob: str) -> int:
        arrAlice = datetime.date(2023, int(arriveAlice[:2]), int(arriveAlice[3:]))
        leaAlice = datetime.date(2023, int(leaveAlice[:2]), int(leaveAlice[3:]))
        arrBob = datetime.date(2023, int(arriveBob[:2]), int(arriveBob[3:]))
        leaBob = datetime.date(2023, int(leaveBob[:2]), int(leaveBob[3:]))

        if arrAlice <= leaBob and arrBob <= leaAlice:
            times = min(leaAlice, leaBob) - max(arrAlice, arrBob)
            return times.days + 1
        return 0

data = [
    "10-01"
    , "10-31"
    , "11-01"
    , "12-31"
]
r = Solution().countDaysTogether(* data)
print(r)

