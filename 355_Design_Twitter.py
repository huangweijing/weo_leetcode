from typing import List
from collections import defaultdict
import heapq


class Post:
    def __init__(self, post_ts: int, tweet_id: int):
        self.post_ts = post_ts
        self.tweet_id = tweet_id

    def __lt__(self, other):
        return self.post_ts < other.post_ts

class Twitter:

    def __init__(self):
        self.user_post = defaultdict(lambda: list[Post]())
        self.followers = defaultdict(lambda: set[int]())
        self.post_cnt = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_post[userId].append(Post(self.post_cnt, tweetId))
        self.post_cnt += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = self.user_post[userId][-min(len(self.user_post[userId]), 10):]
        heapq.heapify(heap)
        for follower in self.followers[userId]:
            for i in range(min(10, len(self.user_post[follower]))):
                post = self.user_post[follower][-1 - i]
                if len(heap) == 10 and post < heap[0]:
                    break
                else:
                    heapq.heappush(heap, post)
                    if len(heap) > 10:
                        heapq.heappop(heap)
        ret_list = []
        while len(heap) > 0:
            ret_list.append(heapq.heappop(heap).tweet_id)
        return ret_list[:: -1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

data = [
    ["Twitter", "postTweet", "postTweet", "unfollow", "getNewsFeed"]
    , [[], [1, 4], [2, 5], [1, 2], [1]]
]
ssa = Twitter()
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret)
    print(ssa.followers)
    result.append(ret)
print(result)