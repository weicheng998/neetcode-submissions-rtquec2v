class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        result = [1] * nums_len

        # Forward pass: result[i] = culmulative prod of all left to i
        prefix = 1
        for i in range(nums_len):
            result[i] = prefix
            prefix *= nums[i]
        
        # Backward pass: multiply the culmulative prod of all right to i
        suffix = 1
        for j in range(nums_len-1, -1, -1):
            result[j] *= suffix
            suffix *= nums[j]

        return result