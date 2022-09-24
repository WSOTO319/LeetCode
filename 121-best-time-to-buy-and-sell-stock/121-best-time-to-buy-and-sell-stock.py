class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf') # set the max profit to start at 0 and set the minimum price set at infinity
        for price in prices: # for each price in the array
            min_price = min(min_price, price) # the minimum price is smallest between the current price we are looking at and the value that minimum price is currently set as 
            profit = price - min_price # our profit is then the current price minus the current minimum price value
            max_profit = max(max_profit, profit) # out max profit is the biggest between the current value of our max profit and the current profit we are getting
        return max_profit # return max profit
    
    
    
   # when finding the lowest of something and/or the highest of something, one idea is to start at the complete opposite of it and work towards it 