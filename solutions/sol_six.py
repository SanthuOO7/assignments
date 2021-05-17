def suma_o_resta(a, b):
	return (a & (1<<b))

def has_lock(v, n):
	suma = 0
	for x in range(1<<n):
		for i in range(n):
			if suma_o_resta(x, i) > 0:
				suma += v[i]
			else:
				suma += -1*v[i]
		if suma%360 == 0:
			return "YES"
		suma = 0
	return "NO"

rotations = int(input())

v = []

for i in range(rotations):
	v.append(int(input()))

print(has_lock(v, rotations))
