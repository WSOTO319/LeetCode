class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l, r = 0, len(s)-1  #set the left pointer to 0(starts at the first letter) and the right pointer to the length of string(starts at last letter)
        while l < r: # while left pointer is not equal to or greater than the right pointer
            while l < r and not s[l].isalnum(): # while left pointer is less than right and the left points at a non-alphanumeric
                l += 1 #move left pointer to the right by 1 
            while l <r and not s[r].isalnum():# while left pointer is less than right and the right points at a non-alphanumeric
                r -= 1 #move right pointer to the left by 1 
            if s[l].lower() != s[r].lower(): # if the current letter at the left pointer and the current letter at the right pointer are not the same
                return False # return false
            l +=1; r -= 1 #move the left pointer to the right by 1 and right pointer to the left by 1
        return True # retun true