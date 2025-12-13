1class ParkingSystem {
2    private slots: number[];
3
4    constructor(big: number, medium: number, small: number) {
5        this.slots = [big, medium, small];
6    }
7
8    addCar(carType: number): boolean {
9        if (this.slots[carType - 1] > 0) {
10            this.slots[carType - 1]--;
11            return true;
12        }
13        return false;
14    }
15}
16
17/**
18 * Your ParkingSystem object will be instantiated and called as such:
19 * var obj = new ParkingSystem(big, medium, small)
20 * var param_1 = obj.addCar(carType)
21 */