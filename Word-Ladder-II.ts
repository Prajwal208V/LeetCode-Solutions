1function findLadders(beginWord: string, endWord: string, wordList: string[]): string[][] {
2    const wordSet = new Set(wordList);
3    if (!wordSet.has(endWord)) return [];
4
5    const parents = new Map<string, string[]>();
6    const res: string[][] = [];
7    const visited = new Set<string>();
8    let level = new Set<string>();
9    level.add(beginWord);
10    visited.add(beginWord);
11    let found = false;
12
13    while (level.size && !found) {
14        const nextLevel = new Set<string>();
15        const localVisited = new Set<string>();
16
17        for (const word of level) {
18            const arr = word.split('');
19            for (let i = 0; i < arr.length; i++) {
20                const original = arr[i];
21                for (let c = 97; c <= 122; c++) {
22                    const ch = String.fromCharCode(c);
23                    if (ch === original) continue;
24                    arr[i] = ch;
25                    const nw = arr.join('');
26                    if (!wordSet.has(nw)) continue;
27                    if (!visited.has(nw)) {
28                        if (!parents.has(nw)) parents.set(nw, []);
29                        parents.get(nw)!.push(word);
30                        if (!localVisited.has(nw)) {
31                            localVisited.add(nw);
32                            nextLevel.add(nw);
33                        }
34                        if (nw === endWord) found = true;
35                    }
36                }
37                arr[i] = original;
38            }
39        }
40
41        for (const w of localVisited) visited.add(w);
42        level = nextLevel;
43    }
44
45    if (!found) return [];
46
47    const path: string[] = [endWord];
48
49    function dfs(word: string) {
50        if (word === beginWord) {
51            res.push([...path].reverse());
52            return;
53        }
54        const ps = parents.get(word);
55        if (!ps) return;
56        for (const p of ps) {
57            path.push(p);
58            dfs(p);
59            path.pop();
60        }
61    }
62
63    dfs(endWord);
64    return res;
65}