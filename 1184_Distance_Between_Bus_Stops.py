class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        dis1, dis2 = 0, 0
        start, destination = min(start, destination), max(start, destination)
        for i in range(start, destination):
            dis1 += distance[i]
        for i in range(destination, len(distance)):
            dis2 += distance[i]
        for i in range(start):
            dis2 += distance[i]
        return min(dis1, dis2)
