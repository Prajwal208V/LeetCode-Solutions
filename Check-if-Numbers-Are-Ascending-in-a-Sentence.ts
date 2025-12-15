1function areNumbersAscending(s: string): boolean {
2    let prev = 0;
3    for (const word of s.split(" ")) {
4        if (!isNaN(Number(word))) {
5            const num = Number(word);
6            if (num <= prev) return false;
7            prev = num;
8        }
9    }
10    return true;
11}