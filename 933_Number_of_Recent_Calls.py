from collections import deque

class RecentCounter:

    def __init__(self):
        self.pings = deque()

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings[0] < t - 3000:
            self.pings.popleft()
        return len(self.pings)
