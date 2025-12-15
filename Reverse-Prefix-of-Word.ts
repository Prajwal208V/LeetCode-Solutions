1function reversePrefix(word: string, ch: string): string {
2    const index = word.indexOf(ch);
3    if (index === -1) return word;
4
5    const reversed = word
6        .slice(0, index + 1)
7        .split('')
8        .reverse()
9        .join('');
10
11    return reversed + word.slice(index + 1);
12}