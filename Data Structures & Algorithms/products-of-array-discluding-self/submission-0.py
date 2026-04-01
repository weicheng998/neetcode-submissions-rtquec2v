class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Build prefix culmulative product
        left = []
        cul_prod = 1
        for n in nums:
            cul_prod *= n
            left.append(cul_prod)
        # Build suffix culmulative product
        right = [0] * len(nums)
        cul_prod = 1
        for i, n in enumerate(reversed(nums)):
            cul_prod *= n
            right[len(nums)-1-i] = cul_prod
        # result[i] = left[i-1] * right[i+1]
        result = []
        for i in range(len(nums)):
            left_prod = left[i - 1] if i > 0 else 1
            right_prod = right[i + 1] if i < len(right) - 1 else 1
            result.append(left_prod * right_prod)
        return result
