1import heapq
2import re
3from typing import List
4
5class Solution:
6    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
7        ans = [0] * numberOfUsers
8        online = [True] * numberOfUsers
9        offline_heap = []
10        all_mentions = 0
11
12        events.sort(key=lambda e: (int(e[1]), -ord(e[0][0])))
13
14        for eventType, t, content in events:
15            timestamp = int(t)
16            while offline_heap and offline_heap[0][0] <= timestamp:
17                _, uid = heapq.heappop(offline_heap)
18                online[uid] = True
19
20            if eventType == "MESSAGE":
21                if content == "ALL":
22                    all_mentions += 1
23                elif content == "HERE":
24                    for uid in range(numberOfUsers):
25                        if online[uid]:
26                            ans[uid] += 1
27                else:
28                    for num in re.findall(r'\d+', content):
29                        uid = int(num)
30                        ans[uid] += 1
31            else:  # "OFFLINE"
32                uid = int(content)
33                online[uid] = False
34                heapq.heappush(offline_heap, (timestamp + 60, uid))
35
36        if all_mentions:
37            for i in range(numberOfUsers):
38                ans[i] += all_mentions
39
40        return ans