class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_water = 0

        while i < j:
            water = (j - i) * min(heights[i], heights[j])
            max_water = max(water, max_water)
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_water