class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {word:i for i, word in enumerate(list1)}
        min_sum = float('inf')
        result = []
        
        for j, word in enumerate(list2):
            if word in index_map:
                i = index_map[word]
                curr_index_sum = i + j
                
                if curr_index_sum < min_sum:
                    result = [word]
                    min_sum = curr_index_sum
                elif curr_index_sum == min_sum:
                    result.append(word)
                    
        return result
                
                
        