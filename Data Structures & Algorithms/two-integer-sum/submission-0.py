class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()
        for i, num in enumerate(nums):
            if num in complements:
                # Check if current num is a complement
                # i.e. There was a num s.t. cur_num + num = target
                return [complements[num], i]
            else:
                # Keep track of [complement, index]
                complements[target - num] = i
        return False


