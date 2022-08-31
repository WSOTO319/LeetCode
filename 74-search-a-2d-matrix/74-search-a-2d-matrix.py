class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0]) # initialize columns and rows
        
        top, bot = 0, ROWS - 1 # initialize top to 0 and bot to ROWS minus 1 which is last Row
        while top <= bot: # while top is less than or equal to bottom
            row = (top + bot) // 2 # get the midrow
            if target > matrix[row][-1]:#if target is greater than the last number in the row
                top = row + 1 # the top goes down a row (greater values)
            elif target < matrix[row][0]: # if target is less than the the first number in the row
                bot = row - 1# bot goes up a row(lesser values)
            else:
                break # else break out of while loop
        if not(top <= bot): #if bottom not greater or equal to top
            return False #return false
        
        row = (top + bot) // 2 #rest of code is finding the number in the row
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2 
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False