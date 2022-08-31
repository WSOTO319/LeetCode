class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #turns the list into a set
        longest = 0 #longest consecutive sequence starts at 0 
        
        for n in nums: # for each number in list
            if (n - 1) not in numSet: #check to see if the number before it is in the set, if not its the start of a sequence
                length = 0 # length is originally at 0 
                while (n + length) in numSet: #while the numbers following are in the set keep adding to the length
                    length += 1
                longest = max(length, longest) #the longest consecutive sequence is the max between current longest and length
        return longest # return longest
        
#Time Complexity: O(n)