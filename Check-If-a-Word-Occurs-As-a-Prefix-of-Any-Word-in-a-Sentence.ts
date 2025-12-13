1function isPrefixOfWord(sentence: string, searchWord: string): number {
2    const words = sentence.split(" ");
3
4    for (let i = 0; i < words.length; i++) {
5        if (words[i].startsWith(searchWord)) {
6            return i + 1;
7        }
8    }
9
10    return -1;
11}