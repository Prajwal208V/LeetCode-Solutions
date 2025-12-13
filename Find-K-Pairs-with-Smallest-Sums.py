1import heapq
2from typing import List
3
4class Solution:
5    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
6        if not nums1 or not nums2 or k == 0:
7            return []
8
9        heap = []
10        res = []
11
12        for i in range(min(k, len(nums1))):
13            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
14
15        while heap and len(res) < k:
16            _, i, j = heapq.heappop(heap)
17            res.append([nums1[i], nums2[j]])
18            if j + 1 < len(nums2):
19                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
20
21        return res