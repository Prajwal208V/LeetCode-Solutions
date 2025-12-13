1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.is_end = False
5
6
7class WordDictionary:
8    def __init__(self):
9        self.root = TrieNode()
10
11    def addWord(self, word: str) -> None:
12        node = self.root
13        for ch in word:
14            if ch not in node.children:
15                node.children[ch] = TrieNode()
16            node = node.children[ch]
17        node.is_end = True
18
19    def search(self, word: str) -> bool:
20        def dfs(node: TrieNode, i: int) -> bool:
21            if i == len(word):
22                return node.is_end
23            ch = word[i]
24            if ch == '.':
25                for child in node.children.values():
26                    if dfs(child, i + 1):
27                        return True
28                return False
29            if ch not in node.children:
30                return False
31            return dfs(node.children[ch], i + 1)
32
33        return dfs(self.root, 0)
34
35
36
37# Your WordDictionary object will be instantiated and called as such:
38# obj = WordDictionary()
39# obj.addWord(word)
40# param_2 = obj.search(word)