import time

x = [1.1,   1.2,   1.3,     1.4,   1.5,   1.6,   1.7,   1.8, 1.9,   2.0,   2.1, 2.2,   2.3,   2.4,   2.5,   2.6]
y = [1.123, 1.234, 1.345, 156.467, 1.578, 1.689, 1.790, 1.812, 1.923, 2.034, 2.145,  2.256, 2.367, 2.478, 2.589, 2.690]

num_iters = 20000
n = len(x)

start = time.time()
for i in range(num_iters):
	for j in range(n):
		x[j] /= y[j]

		x[j] += 0
		x[j] -= 0
end = time.time()

print x
print end - start
