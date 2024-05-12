class Solution:
    def reformatDate(self, date: str) -> str:
        const_mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        mon_dict = {m: i + 1 for i, m in enumerate(const_mon)}
        date_arr = date.split(sep=" ")
        dd = date_arr[0][:-2].rjust(2, "0")
        mm = str(mon_dict[date_arr[1]]).rjust(2, "0")
        yyyy = date_arr[2]
        return f"{yyyy}-{mm}-{dd}"

data = "20th Oct 2052"
r = Solution().reformatDate(data)
print(r)

