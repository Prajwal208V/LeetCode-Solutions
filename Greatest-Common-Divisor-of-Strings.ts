1function gcdOfStrings(str1: string, str2: string): string {
2    if (str1 + str2 !== str2 + str1) return "";
3
4    function gcd(a: number, b: number): number {
5        while (b !== 0) {
6            const t = a % b;
7            a = b;
8            b = t;
9        }
10        return a;
11    }
12
13    const g = gcd(str1.length, str2.length);
14    return str1.slice(0, g);
15}
16