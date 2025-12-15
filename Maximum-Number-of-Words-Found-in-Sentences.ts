1function mostWordsFound(sentences: string[]): number {
2    let max = 0;
3    for (const s of sentences) {
4        max = Math.max(max, s.split(" ").length);
5    }
6    return max;
7}