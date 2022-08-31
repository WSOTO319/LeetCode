class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """         
                
        left, right = 0, len(numbers)-1 #left pointer and right pointer
        while left < right: #while left hasnt reached right pointer
            sumofnums = numbers[left] + numbers[right] # sum of the numbers that each pointer is pointing at
            if sumofnums == target: #if these numbers add to the target
                return [left+1, right+1] # return the index of these numbers, plus one because it must be above zero(non compsci way of counting)
            elif sumofnums < target: # if the sum is less than target, move the left pointer up
                left += 1
            else:
                right -= 1 # if sum is higher than target move right pointer down 
                #moving the pointer is decided because list is in non-decreasing order