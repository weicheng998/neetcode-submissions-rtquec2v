class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position, speed, and time to finish
        cars = [(pos, speed, (target - pos) / speed) for pos, speed in zip(position, speed)]
        # Sort according to the position
        cars.sort()
        # Use a monotonic stack to keep track of fleets
        leader = cars.pop()
        n_fleet = 1
        while cars:
            if cars[-1][2] <= leader[2]:
                # The top of the stack will catch up the current leader
                cars.pop()
            else:
                leader = cars.pop()
                n_fleet += 1
        return n_fleet