class Solution:
    def maxSubarrayXOR (self, N, arr):
        # code here 
        ans = -2147483648     #Initialize result
  
        # Pick starting points of subarrays
        for i in range(N):
             
            # to store xor of current subarray
            curr_xor = 0
      
            # Pick ending points of
            # subarrays starting with i
            for j in range(i,N):
             
                curr_xor = curr_xor ^ arr[j]
                ans = max(ans, curr_xor)
             
         
        return ans
        