from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        # count[num] = freq
        count = Counter(nums)
        # Create a bucket list: index ~ freq, val ~ [nums appeared with this freq]
        buckets = [[] for i in range(len(nums) + 1)]
        # Fill in the bucket
        for num, freq in count.items():
            buckets[freq].append(num)
        # Collect the top k most freq nums
        i = 0
        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                i += 1
                if i == k:
                    break
            if i == k:
                break
        return result
        