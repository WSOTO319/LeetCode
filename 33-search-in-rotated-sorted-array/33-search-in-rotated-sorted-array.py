class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 #initialize left pointer and right pointer
        
        while l <= r: # while the left pointer is less than the right
            mid = (l + r) // 2 # initialize mid pointer
            if target == nums[mid]: # if number at mid pointer is the target
                return mid # return the number mid pointer index
            
            if nums[l] <= nums[mid]: # if the number at the mid poijnter is greater than the number at left pointer
                if target > nums[mid] or target < nums[l]: # if the target is greater than the number at mid pointer OR the target is less than the number at the left pointer 
                    l = mid + 1 # left pointer is set to the index after the mid pointer
                else: # else, right pointer is set to the index before the mid pointer 
                    r = mid - 1 
            else:# else
                if target < nums[mid] or target > nums[r]:# if the target is less then the number at the mid pointer OR the target is greater than the number at right pointer 
                    r = mid - 1 # right pointer is set at the index before the mid pointer
                else:# else, left pointer is set to the the index after the mid pointer 
                    l = mid + 1
                    
        return -1 # return -1 if target not found