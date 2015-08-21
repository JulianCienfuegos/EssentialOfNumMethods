import random
import time
 
# Set up some random matrices.
a = []
b = []
c = []
N = 200
for i in range(N):
                a.append([random.random() for i in range(N)])
                b.append([random.random() for i in range(N)])
 
# Run the code in the non-permuted way
num_iters = 100
 
A = []
B = []
C = []
for i in range(N):
                A.append(a[i])
                B.append(b[i])
                C.append([0 for i in range(N)])
 
start = time.time()
for it in range(num_iters):
                for row in range(N):
                                for col in range(N):
                                                for k in range(N):
                                                                C[row][k] += (A[row][k]*B[k][col])
end = time.time()
print end - start
 
A = []
B = []
C = []
 
for i in range(N):
                A.append(a[i])
                B.append(b[i])
                C.append([0 for i in range(N)])
# run the code in the permuted way
start = time.time()
for it in range(num_iters):
                for k in range(N):
                                for col in range(N):
                                                for row in range(N):
                                                                C[row][k] += (A[row][k]*B[k][col])
end = time.time()
print end - start