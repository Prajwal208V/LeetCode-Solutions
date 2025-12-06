1function largestNumber(nums: number[]): string {
2  const arr = nums.map(String);
3  arr.sort((a, b) => {
4    const ab = a + b;
5    const ba = b + a;
6    if (ab > ba) return -1;
7    if (ab < ba) return 1;
8    return 0;
9  });
10  if (arr[0] === "0") return "0";
11  return arr.join("");
12}
13