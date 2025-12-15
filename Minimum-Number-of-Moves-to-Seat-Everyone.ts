1function minMovesToSeat(seats: number[], students: number[]): number {
2    seats.sort((a, b) => a - b);
3    students.sort((a, b) => a - b);
4
5    let moves = 0;
6    for (let i = 0; i < seats.length; i++) {
7        moves += Math.abs(seats[i] - students[i]);
8    }
9
10    return moves;
11}