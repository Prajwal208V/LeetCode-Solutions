1function minimumSum(num: number): number {
2    const d = num.toString().split('').map(Number).sort((a,b)=>a-b);
3    return (d[0]*10 + d[2]) + (d[1]*10 + d[3]);
4}