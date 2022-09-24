class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}','[':']'} #map for the open and closing pairs
        stack = [] #initialize a stack
        for i in s: # go through each item in the string
            if i in d:  #if the item is a key in the the map
                stack.append(i) #append the item to the stack
            elif len(stack) == 0 or d[stack.pop()] != i:  #elif the stack is empty OR the value being popped is not equal to the item/key's value 
                return False # return False
        return len(stack) == 0 #AFTER looping through the whole string return True if the stack is empty