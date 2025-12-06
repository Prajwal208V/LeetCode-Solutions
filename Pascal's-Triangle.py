1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        res = [[1]]
4        for _ in range(1, numRows):
5            prev = res[-1]
6            row = [1] + [prev[i] + prev[i+1] for i in range(len(prev)-1)] + [1]
7            res.append(row)
8        return res
9