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
		counter = {}
		for x in res:
			if x not in counter:
				counter[x] = res.count(x)
		# print(counter)
		s = ""
		for k, v in counter.items():
			s += "{0}^{1}*".format(k, v)
		if s[0] == "2":
			print(s[:-1])
		else:
			print("2^0*"+s[:-1])