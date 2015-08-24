import random
import time
 
def print_mat(M):
        for r in M:
                print r
        print '\n\n'

# Set up some random matrices.
a = []
b = []
c = []
N = 3
for i in range(N):
                a.append([random.randint(1, 4) for i in range(N)])
                b.append([random.randint(1, 4) for i in range(N)])
 
# Run the code in the non-permuted way
num_iters = 1
 
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
                                                                C[row][col] += (A[row][k]*B[k][col])
end = time.time()
print end - start
print_mat(A)
print_mat(B)
print_mat(C)
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
                                                                C[row][col] += (A[row][k]*B[k][col])
end = time.time()
print end - start

print_mat(A)
print_mat(B)
print_mat(C)