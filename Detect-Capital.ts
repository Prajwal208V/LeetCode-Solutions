1function detectCapitalUse(word: string): boolean {
2    const allUpper = word === word.toUpperCase();
3    const allLower = word === word.toLowerCase();
4    const firstUpper = word[0] === word[0].toUpperCase() && word.slice(1) === word.slice(1).toLowerCase();
5    return allUpper || allLower || firstUpper;
6}
7