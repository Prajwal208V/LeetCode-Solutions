1function firstPalindrome(words: string[]): string {
2    for (const word of words) {
3        if (word === word.split('').reverse().join('')) {
4            return word;
5        }
6    }
7    return "";
8}