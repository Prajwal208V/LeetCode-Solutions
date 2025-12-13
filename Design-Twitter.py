1import heapq
2from typing import List
3from collections import defaultdict
4
5class Twitter:
6
7    def __init__(self):
8        self.time = 0
9        self.tweets = defaultdict(list)
10        self.following = defaultdict(set)
11
12    def postTweet(self, userId: int, tweetId: int) -> None:
13        self.time += 1
14        self.tweets[userId].append((self.time, tweetId))
15
16    def getNewsFeed(self, userId: int) -> List[int]:
17        heap = []
18        users = self.following[userId] | {userId}
19
20        for u in users:
21            for t in self.tweets[u][-10:]:
22                heapq.heappush(heap, t)
23                if len(heap) > 10:
24                    heapq.heappop(heap)
25
26        return [tweetId for _, tweetId in sorted(heap, reverse=True)]
27
28    def follow(self, followerId: int, followeeId: int) -> None:
29        if followerId != followeeId:
30            self.following[followerId].add(followeeId)
31
32    def unfollow(self, followerId: int, followeeId: int) -> None:
33        self.following[followerId].discard(followeeId)
34
35
36
37# Your Twitter object will be instantiated and called as such:
38# obj = Twitter()
39# obj.postTweet(userId,tweetId)
40# param_2 = obj.getNewsFeed(userId)
41# obj.follow(followerId,followeeId)
42# obj.unfollow(followerId,followeeId)