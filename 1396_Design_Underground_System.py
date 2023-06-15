class UndergroundSystem:

    def __init__(self):
        self.in_out_time_sum = dict[str, int]()
        self.in_out_time_cnt = dict[str, int]()
        self.id_in_station = dict[int, str]()
        self.id_in_time = dict[int, str]()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_in_station[id] = stationName
        self.id_in_time[id] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        key = self.id_in_station[id] + "," + stationName
        time = t - self.id_in_time[id]
        if key not in self.in_out_time_sum:
            self.in_out_time_sum[key] = 0
            self.in_out_time_cnt[key] = 0
        self.in_out_time_sum[key] += time
        self.in_out_time_cnt[key] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + "," + endStation
        return self.in_out_time_sum[key] / self.in_out_time_cnt[key]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)