class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n #initialize bottom row
        
        for i in range (m - 1): # go through all bottom rows except last one
            newRow = [1] * n # for each row we will compute new row
            for j in range(n - 2, -1, -1):#go through every column except the last since every value in each row for that column will equal 1; go in reverse order
                newRow[j] = newRow[j + 1] + row[j] #add value from the right and value below to the postion 
            row = newRow #set row to the new row
        return row[0] # return the first value of new row