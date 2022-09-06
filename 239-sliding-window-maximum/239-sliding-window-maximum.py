class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = [] # initialize output array
        q = collections.deque() # initialize deque
        l = r = 0 # set left and right to 0
        
        while r < len(nums): # while right is less than the length of nums
            
            while q and nums[q[-1]] < nums[r]: #while queue is not empty and last element on queue is less than the nums value, pop smaller values from the queue
                q.pop()
            q.append(r)
            
            if l > q[0]: # remove left val from window
                q.popleft()
                
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
        