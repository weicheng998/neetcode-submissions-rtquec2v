class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        result = []

        for i, num in enumerate(nums_sorted):
            # Early termination: smallest number > 0, no triplet possible
            if num > 0:
                break

            # Skip duplicate values of i
            if i > 0 and num == nums_sorted[i - 1]:
                continue

            j, k = i + 1, len(nums_sorted) - 1
            while j < k:
                s = num + nums_sorted[j] + nums_sorted[k]
                if s == 0:
                    result.append([num, nums_sorted[j], nums_sorted[k]])
                    # Skip duplicates for j and k
                    while j < k and nums_sorted[j] == nums_sorted[j + 1]:
                        j += 1
                    while j < k and nums_sorted[k] == nums_sorted[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1

        return result