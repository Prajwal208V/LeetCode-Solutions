1/**
2 * // This is the interface that allows for creating nested lists.
3 * // You should not implement it, or speculate about its implementation
4 * class NestedInteger {
5 *     If value is provided, then it holds a single integer
6 *     Otherwise it holds an empty nested list
7 *     constructor(value?: number) {
8 *         ...
9 *     };
10 *
11 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
12 *     isInteger(): boolean {
13 *         ...
14 *     };
15 *
16 *     Return the single integer that this NestedInteger holds, if it holds a single integer
17 *     Return null if this NestedInteger holds a nested list
18 *     getInteger(): number | null {
19 *         ...
20 *     };
21 *
22 *     Set this NestedInteger to hold a single integer equal to value.
23 *     setInteger(value: number) {
24 *         ...
25 *     };
26 *
27 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
28 *     add(elem: NestedInteger) {
29 *         ...
30 *     };
31 *
32 *     Return the nested list that this NestedInteger holds,
33 *     or an empty list if this NestedInteger holds a single integer
34 *     getList(): NestedInteger[] {
35 *         ...
36 *     };
37 * };
38 */
39
40function deserialize(s: string): NestedInteger {
41    if (s[0] !== '[') return new NestedInteger(parseInt(s));
42    const stack: NestedInteger[] = [];
43    let num: string | null = null;
44    for (let i = 0; i < s.length; i++) {
45        const ch = s[i];
46        if (ch === '[') {
47            stack.push(new NestedInteger());
48        } else if (ch === '-' || (ch >= '0' && ch <= '9')) {
49            num = (num ?? '') + ch;
50        } else if (ch === ',' || ch === ']') {
51            if (num !== null) {
52                const val = parseInt(num);
53                stack[stack.length - 1].add(new NestedInteger(val));
54                num = null;
55            }
56            if (ch === ']' && stack.length > 1) {
57                const ni = stack.pop() as NestedInteger;
58                stack[stack.length - 1].add(ni);
59            }
60        }
61    }
62    return stack[0];
63}
64