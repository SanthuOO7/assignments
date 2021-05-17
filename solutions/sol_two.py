class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here
        count = 0
        while N!=0:
            N = N & (N<<1)
            count+=1
            
        return count
