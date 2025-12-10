1function largestRectangleArea(heights: number[]): number {
2    const stack: number[] = [];
3    let maxArea = 0;
4    const n = heights.length;
5
6    for (let i = 0; i <= n; i++) {
7        const h = i === n ? 0 : heights[i];
8        while (stack.length && h < heights[stack[stack.length - 1]]) {
9            const height = heights[stack.pop() as number];
10            const width = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
11            maxArea = Math.max(maxArea, height * width);
12        }
13        stack.push(i);
14    }
15
16    return maxArea;
17}