1function findLongestWord(s: string, dictionary: string[]): string {
2    const isSub = (word: string): boolean => {
3        let i = 0
4        for (const c of s) if (i < word.length && word[i] === c) i++
5        return i === word.length
6    }
7
8    dictionary.sort((a, b) =>
9        b.length !== a.length ? b.length - a.length : a.localeCompare(b)
10    )
11
12    for (const word of dictionary) {
13        if (isSub(word)) return word
14    }
15    return ""
16}