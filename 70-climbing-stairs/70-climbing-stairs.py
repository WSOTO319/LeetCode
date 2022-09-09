class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: # if n = 1 then cleraly theres only one way of climbing stair
            return 1 # so return 1
        a, b = 1, 2 
        for i in xrange(2, n): # for range from 2 to n 
            tmp = b #temporary variable holds b value  
            b = a+b # b is set to a + b, so for example if n is two b will end up being 3 
            a = tmp # a variable is set to the temp variable for next time in loop 
        return b