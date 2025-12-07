1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.end = False
5
6class Trie:
7    def __init__(self):
8        self.root = TrieNode()
9
10    def insert(self, word: str) -> None:
11        node = self.root
12        for ch in word:
13            if ch not in node.children:
14                node.children[ch] = TrieNode()
15            node = node.children[ch]
16        node.end = True
17
18    def search(self, word: str) -> bool:
19        node = self.root
20        for ch in word:
21            if ch not in node.children:
22                return False
23            node = node.children[ch]
24        return node.end
25
26    def startsWith(self, prefix: str) -> bool:
27        node = self.root
28        for ch in prefix:
29            if ch not in node.children:
30                return False
31            node = node.children[ch]
32        return True
33
34
35
36# Your Trie object will be instantiated and called as such:
37# obj = Trie()
38# obj.insert(word)
39# param_2 = obj.search(word)
40# param_3 = obj.startsWith(prefix)