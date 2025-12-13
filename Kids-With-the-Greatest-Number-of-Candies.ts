1function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
2    const maxCandies = Math.max(...candies);
3    return candies.map(c => c + extraCandies >= maxCandies);
4}