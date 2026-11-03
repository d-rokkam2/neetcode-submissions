class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        max_area = float('-inf')

        while left < right:
            
            width = right - left 
            curr_area = min(heights[left], heights[right]) * width
            max_area = max(max_area, curr_area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_area
