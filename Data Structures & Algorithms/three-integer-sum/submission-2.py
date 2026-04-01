class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_sorted = sorted(nums)

        for i, num in enumerate(nums_sorted):
            j, k = i + 1, len(nums_sorted) - 1
            while j < k:
                s = nums_sorted[j] + nums_sorted[k] + num
                if s == 0:
                    triplet = [num, nums_sorted[j], nums_sorted[k]]
                    # if triplet not in result:
                    result.append(triplet)
                    break
                elif s < 0:
                    j += 1
                elif s > 0:
                    k -= 1

        return result