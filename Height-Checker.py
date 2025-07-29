class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights[:]
        has_swapped = True
        result = 0 
        
        while has_swapped:
            has_swapped = False
            for i in range(len(expected)-1):
                if expected[i+1] < expected[i]:
                    expected[i], expected[i+1] = expected[i+1], expected[i]
                    has_swapped = True
                    
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result += 1
        return result