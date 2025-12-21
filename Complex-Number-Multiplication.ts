1function complexNumberMultiply(num1: string, num2: string): string {
2    const [a, b] = num1.replace('i', '').split('+').map(Number);
3    const [c, d] = num2.replace('i', '').split('+').map(Number);
4    return `${a * c - b * d}+${a * d + b * c}i`;
5}