1class Solution:
2    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
3        pref = [0]
4        for x in nums:
5            pref.append(pref[-1] + x)
6
7        def sort_count(lo: int, hi: int) -> int:
8            if hi - lo <= 1:
9                return 0
10            mid = (lo + hi) // 2
11            cnt = sort_count(lo, mid) + sort_count(mid, hi)
12            j = k = mid
13            for left in pref[lo:mid]:
14                while k < hi and pref[k] - left < lower:
15                    k += 1
16                while j < hi and pref[j] - left <= upper:
17                    j += 1
18                cnt += j - k
19            pref[lo:hi] = sorted(pref[lo:hi])
20            return cnt
21
22        return sort_count(0, len(pref))
23