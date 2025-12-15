1function prefixCount(words: string[], pref: string): number {
2    return words.filter(w => w.startsWith(pref)).length;
3}