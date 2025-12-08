1class Solution:
2    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
3        for row in image:
4            row.reverse()
5            for i in range(len(row)):
6                row[i] ^= 1
7        return image
8