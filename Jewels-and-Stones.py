1class Solution:
2    def numJewelsInStones(self, jewels: str, stones: str) -> int:
3        jewel_set = set(jewels)
4        return sum(stone in jewel_set for stone in stones)