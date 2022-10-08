import bisect

class TimeMap:

    def __init__(self):
        self.time_val = dict[int, str]()
        self.data = dict[str, list[int]]()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = list[int]()
        self.data[key].append(timestamp)
        self.time_val[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        time_list = self.data[key]
        idx = bisect.bisect_right(time_list, timestamp) - 1
        if idx == -1:
            return ""
        else:
            return self.time_val[time_list[idx]]


d = [1,4,8,12,9]
r = bisect.bisect_right(d, 7)
print(r)