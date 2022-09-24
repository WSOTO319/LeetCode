class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, b in enumerate(nums): #enumerates nums
            # a + b = target -> a = target - b soo 
            a = target - b
            if a in seen:# if the number has been seen 
                return [seen[a], i] # return a's index, and the current index of b 
            seen[b] = i #else store the number in the seen dictionary with its value being its index