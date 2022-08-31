class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0 # initialize result
        l, r = 0, len(height) - 1 #left pointer at 0 and right pointer at the length of height minus 1
        
        while l < r: # while left pointer is smaller than the right 
            area = (r - l) * min(height[l], height[r]) # the area is the distance between right and left pointer multiplied by the minimum height of both pointers
            res = max(res, area) # result is the max between the current result and current area
            
            if height[l] < height[r]: # if the height of the left pointer is less than the height of the right pointer, move the left pointer up
                l += 1
            else:# else, move the right pointer down
                r -= 1
                
        return res # return result
                