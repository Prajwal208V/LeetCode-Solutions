1class Solution:
2    def uniqueMorseRepresentations(self, words: List[str]) -> int:
3        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
4                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
5                 "..-","...-",".--","-..-","-.--","--.."]
6        
7        # Convert each word to morse code and add to set
8        transformations = set()
9        for word in words:
10            morse_word = ''.join(morse[ord(char) - ord('a')] for char in word)
11            transformations.add(morse_word)
12        
13        return len(transformations)