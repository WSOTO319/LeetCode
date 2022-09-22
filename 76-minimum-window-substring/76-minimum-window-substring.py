class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": #if substring is empty just return ""
            return ""

        countT, window = {}, {} #hashmpas for counT(which counts the letter in substrings) and for window(which counts the letters in the current window)
        for c in t: #for each letter in t
            countT[c] = 1 + countT.get(c, 0)#the value of c in CountT will be incremented. get just allows for c to be added to hashmap if not already in and be set to 0, which will end up being 1 since one is added 

        have, need = 0, len(countT) # initialize the have variable and the need variable so we can use them to see what we have and we need 
        res, resLen = [-1, -1], float("infinity")#set result and resultlength
        l = 0# initialize left pointer 
        
        for r in range(len(s)): # iterate through every character in s
            c = s[r] #get the character and put it in variable c 
            window[c] = 1 + window.get(c, 0) # update current window hashmap by adding the character to it or incrementing it by one if already in hashmap

            if c in countT and window[c] == countT[c]: # if character is in the countT hashmap AND the value for the character in each hashmap are the same 
                have += 1 #increment have by 1 

            while have == need: # while have is equal to need
                # update our result
                if (r - l + 1) < resLen: #if current length of string is less than current resultlength
                    res = [l, r]#update result to left and right pointer
                    resLen = r - l + 1#updater resultlength
                
                window[s[l]] -= 1# pop from the left of our window
                if s[l] in countT and window[s[l]] < countT[s[l]]:# if the most left character is in countT hashmap and the value of the character in the window is less than the value of it in the counT
                    have -= 1 #decrement the have variable by 1 
                l += 1 # move left pointer to the right by 1
        l, r = res # left pointer and right pointer is equal to result 
        return s[l : r + 1] if resLen != float("infinity") else "" #return string s from left pointer to right pointer plus one if result length not equal to infinity(no result) then return " "