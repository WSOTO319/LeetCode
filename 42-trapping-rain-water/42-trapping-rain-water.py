class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        l, r = 0, len(height) - 1 # initialize left and right pointer variables
        leftMax, rightMax = height[l], height[r] #initilaize the left and right max
        res = 0 #initialize result variabe
        
        while l < r: #while left pointer is less than right pointer 
            if leftMax < rightMax: # if leftMax is less than rightMax 
                l += 1 # move the left pointer up
                leftMax = max(leftMax, height[l]) # leftMax will be the maximum between the current leftMax and the new height at the left pointer
                res += leftMax - height[l] # add the difference between the leftMax and the current height to the result
                
            else: #if left pointer is not less than the right pointer
                r -= 1 # move the right pointer down by one 
                rightMax = max(rightMax, height[r]) #rightMax is the maximum between the current rightMax and the new height at the right pointer 
                res += rightMax - height[r] # add the difference between the rightMax and the current height to the result 
                
        return res #return the result