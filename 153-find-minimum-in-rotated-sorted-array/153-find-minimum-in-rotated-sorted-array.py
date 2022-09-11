class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # intialize res as first number in array 
        l, r = 0, len(nums) - 1 # initialize left and right pointer 
        
        while l <= r: # while left pointer is less than or equal to right pointer 
            if nums[l] < nums[r]: # if number at left pointer is less than number at right pointer,
                res = min(res, nums[l]) # result is equal to the minimum between the current res and the number at the left pointer
                break # break the loop
                
            m = (l + r) // 2 # mid pointer initialized 
            res = min(res, nums[m]) # result is minimum between the current res and the number at the middle pointer 
            if nums[m] >= nums[l]: # if num at middle pointer is greater than or equal to number at left pointer 
                l = m + 1 # left pointer is set to the number after the middle pointer 
            else: # else, right pointer is set to the number before the middle pointer 
                r = m - 1
        return res # return the result 