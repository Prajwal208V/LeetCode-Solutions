class Solution:
    def maxArea(self, height: List[int]) -> int:
        Left, Right = 0, len(height) - 1
        best = 0

        while Left < Right:
            h = min(height[Left], height[Right])
            width = Right - Left
            best = max(best, h * width)

            if height[Left] < height[Right]:
                Left += 1
            else:
               Right -= 1 
        return best

        

        