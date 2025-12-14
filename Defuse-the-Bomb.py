1from typing import List
2
3class Solution:
4    def decrypt(self, code: List[int], k: int) -> List[int]:
5        n = len(code)
6        if k == 0:
7            return [0] * n
8        
9        result = [0] * n
10        code_extended = code * 2
11        
12        if k > 0:
13            window_sum = sum(code_extended[1:k+1])
14            for i in range(n):
15                result[i] = window_sum
16                window_sum += code_extended[i + k + 1]
17                window_sum -= code_extended[i + 1]
18        else:
19            k = -k
20            window_sum = sum(code_extended[n-k:n])
21            for i in range(n):
22                result[i] = window_sum
23                window_sum += code_extended[i + n]
24                window_sum -= code_extended[i + n - k]
25        
26        return result