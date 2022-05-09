#leetcode practice question 11
#determine the maximum possible area given an array of heights which would hold the most water possible

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        
        while l < r:
            if height[l] <= height[r]:
                newArea = height[l] * (r - l)
                l += 1
                
            elif height[l] > height[r]:
                newArea = height[r] * (r - l)
                r -= 1
                
            if newArea > area:
                area = newArea
        
        return area
                