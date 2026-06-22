class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position, speed, and time to finish
        cars = list(zip(position, speed))
        # Sort according to the position
        cars.sort()
        # Use a monotonic stack to keep track of fleets
        leader = cars.pop()
        leader_time_finish = (target - leader[0]) / leader[1]
        n_fleet = 1
        while cars:
            top_time_finish = (target - cars[-1][0]) / cars[-1][1]
            if  top_time_finish <= leader_time_finish:
                # The top of the stack will catch up the current leader
                cars.pop()
            else:
                leader = cars.pop()
                leader_time_finish = top_time_finish
                n_fleet += 1
        return n_fleet
