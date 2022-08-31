class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         
        if len(s) != len(t):# cant be an anagram if not the same length so if not same length reurn False
            return False
        
        countS, countT = {}, {} # create hashmaps for each to count the occurence of each character 
        
        for i in range(len(s)):# since t and s are the same character you could use len s or len t; for every character in the words
            countS[s[i]] = 1 + countS.get(s[i], 0) # this basically checks the character and increments its value; using .get if the character is not in the map yet it will use the second parameter as its default value 
            countT[t[i]] = 1 + countT.get(t[i], 0) # does the same thing for t string
            
        for c in countS:# iterate through the hashmaps and make sure each character occurs the same amount of times 
            if countS[c] != countT.get(c, 0): # if the occurences(values) of each character(key) are not the same, it is not an anagram so return False (also uses .get for countT in case a character in s isnt in t)
                return False
        
        return True # else return True
            
        
        #Time Complexity: O(s + t)
        #Space Complexity: O(s + t)
        
#--------------------------------------------------------------------------------------------------------------------------        
        #technically you can do the above with one line of code using:
        #return Counter(s) == Counter(t) 
        #however some might see this as an easy way out and cheating 
        
        #also you can save on memory by using:
        #return sorted(s) == sorted(t)
        #however it depends on how sorted might be seen by interviewer and might even be asked to make a sorting algorithm    