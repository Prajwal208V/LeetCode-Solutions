1function reorderSpaces(text: string): string {
2    const spaceCount = [...text].filter(ch => ch === ' ').length;
3    const words = text.trim().split(/\s+/);
4
5    if (words.length === 1) {
6        return words[0] + " ".repeat(spaceCount);
7    }
8
9    const gaps = words.length - 1;
10    const spacesBetween = Math.floor(spaceCount / gaps);
11    const extraSpaces = spaceCount % gaps;
12
13    return words.join(" ".repeat(spacesBetween)) + " ".repeat(extraSpaces);
14}