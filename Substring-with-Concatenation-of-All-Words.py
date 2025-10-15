from collections import Counter # Import Counter for word frequency counting

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: # Check for empty input
            return [] # Return empty list if input is invalid

        word_len = len(words[0]) # Get the length of each word
        num_words = len(words) # Get the number of words
        total_len = word_len * num_words # Calculate total length of concatenated words
        word_count = Counter(words) # Count frequency of each word in words
        result = [] # Initialize result list

        for i in range(len(s) - total_len + 1): # Slide window over s
            seen = {} # Dictionary to count words seen in current window
            for j in range(num_words): # For each word in the window
                word_index = i + j * word_len # Calculate start index of current word
                word = s[word_index:word_index + word_len] # Extract the word
                if word in word_count: # If word is in the original list
                    seen[word] = seen.get(word, 0) + 1 # Increment count in seen
                    if seen[word] > word_count[word]: # If seen too many times
                        break # Break out of loop
                else:
                    break # Break if word not in original list
            if seen == word_count: # If seen matches original word count
                result.append(i) # Add starting index to result

        return result # Return the result list