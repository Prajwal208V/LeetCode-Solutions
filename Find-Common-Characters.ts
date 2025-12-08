1function commonChars(words: string[]): string[] {
2    const base = new Array(26).fill(0);
3    for (const ch of words[0]) {
4        base[ch.charCodeAt(0) - 97]++;
5    }
6
7    for (let i = 1; i < words.length; i++) {
8        const cnt = new Array(26).fill(0);
9        for (const ch of words[i]) {
10            cnt[ch.charCodeAt(0) - 97]++;
11        }
12        for (let j = 0; j < 26; j++) {
13            base[j] = Math.min(base[j], cnt[j]);
14        }
15    }
16
17    const res: string[] = [];
18    for (let i = 0; i < 26; i++) {
19        for (let k = 0; k < base[i]; k++) {
20            res.push(String.fromCharCode(97 + i));
21        }
22    }
23    return res;
24}
25