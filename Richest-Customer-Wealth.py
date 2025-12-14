1from typing import List
2
3class Solution:
4    def maximumWealth(self, accounts: List[List[int]]) -> int:
5        return max(sum(customer) for customer in accounts)