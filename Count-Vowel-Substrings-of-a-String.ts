1function countVowelSubstrings(word: string): number {
2    const vowels = new Set(['a','e','i','o','u']);
3    let res = 0;
4
5    for (let i = 0; i < word.length; i++) {
6        const set = new Set<string>();
7        for (let j = i; j < word.length; j++) {
8            if (!vowels.has(word[j])) break;
9            set.add(word[j]);
10            if (set.size === 5) res++;
11        }
12    }
13    return res;
14}