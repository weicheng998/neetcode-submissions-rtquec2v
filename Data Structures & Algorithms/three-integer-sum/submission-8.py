class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        result = []

        i = 0
        while i < len(nums_sorted):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                i += 1
                continue

            j, k = i + 1, len(nums_sorted) - 1
            while j < k:
                s = nums_sorted[i] + nums_sorted[j] + nums_sorted[k]
                if s == 0:
                    result.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                    while j < k and nums_sorted[j] == nums_sorted[j + 1]:
                        j += 1
                    while j < k and nums_sorted[k] == nums_sorted[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                elif s > 0:
                    k -= 1

            i += 1
            
        return result