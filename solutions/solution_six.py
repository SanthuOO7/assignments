
# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # finding the sum of whole array
        arr = A
        total_sum = sum(arr)
        leftsum = 0
        for i, num in enumerate(arr):
             
            # total_sum is now right sum
            # for index i
            total_sum -= num
             
            if leftsum == total_sum:
                return i+1
            leftsum += num
          
          # If no equilibrium index found,
          # then return -1
        return -1