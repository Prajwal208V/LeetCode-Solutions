1function isLongPressedName(name: string, typed: string): boolean {
2    let i = 0, j = 0;
3
4    while (j < typed.length) {
5        if (i < name.length && name[i] === typed[j]) {
6            i++;
7        } else if (j === 0 || typed[j] !== typed[j - 1]) {
8            return false;
9        }
10        j++;
11    }
12
13    return i === name.length;
14}
15