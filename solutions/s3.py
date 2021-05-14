

# Write your code here
def primeFactors(N):
    p,i = 2,1               # prime divisor and increment
    while p*p<=N:           # no need to go beyond √N 
        while N%p == 0:     # if is integer divisor
            yield p         # output prime divisor
            N //= p         # remove it from the number
        p,i = p+i,2         # advance to next potential divisor 2, 3, 5, ... 
    if N>1: yield N         # remaining value is a prime if not 1

if __name__ == "__main__":
	for i in range(int(input())):
		res = primeFactors(int(input()))
		res = sorted(list(res))
		print(res[-1])