#Sum-Of-Consecutive-Numbers
## I wrote N+1 because if I wrote N the number N would not be included.

N = int(input())
sums = 0
for top in range(1,N+1):  
    sums += top
print(sums)
