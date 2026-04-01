class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        nums_set = set(nums)

        for num in nums_set:
            # If this is a starting number
            if num - 1 not in nums_set:
                count = 0
                while num + count in nums_set:
                    count += 1
                max_count = max(max_count, count)
        
        return max_count