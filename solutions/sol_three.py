class Solution:
    def convertEvenBitToZero (ob, n):
        # code here 
        temp=n
        i=0
        while(n>0):
            temp=temp&~(1<<i)
            i+=2
            n=n>>2
        return temp