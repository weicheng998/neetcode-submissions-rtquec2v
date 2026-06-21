class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position and speed into a tuple
        cars: list[tuple] = [(position[i], speed[i]) for i in range(len(position))]
        # Sort the cars based on the position
        cars.sort()
        # Use a stack to keep track of the collisions
        cur = cars.pop()
        num_fleet = 1
        while cars:
            time_finish = (target - cur[0]) / cur[1]
            if cars[-1][1] * time_finish >= target - cars[-1][0]:
                # The cars will catch up
                cars.pop()
            else:
                num_fleet += 1
                cur = cars.pop()
        return num_fleet
