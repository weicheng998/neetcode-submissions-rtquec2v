class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        for num in nums_set:
            # If num is a starting number of a sequence
            if num-1 not in nums_set:
                count = 0
                for i in range(len(nums_set)):
                    if num+i in nums_set:
                        count += 1
                    else:
                        break
                max_count = max(max_count, count)
        
        return max_count