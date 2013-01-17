#! /usr/bin/env python
#for input:
#    A=[0,1,0,2,1,0,1,3,2,1,2,1]
#    N= sizeof(A)
#
#    compute B[] where B[i]= Max(A[0..i])
#    B=[0,1,1,2,2,2,2,3,3,3,3,3]
#
#    compute C[] where C[i]= Max(A[i..N])
#    C=[3,3,3,3,3,3,3,3,2,2,2,1]
#
#    compute D[] where D[i]=Min(B[i],C[I])
#    D=[0,1,1,2,2,2,2,3,2,2,2,1]
#
#    compute E[] where E[i]=D[i]-A[i]
#    E[i]=[0,0,1,0,1,2,1,0,0,1,0,0]
#
#    the answer is sum(E[i])
#    the complexity is O(N)
def f(l):
    max_from_left = []
    max_from_right = []
    min_of_max = []
    max = 0
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
        max_from_left.append(max)
    max = 0
    for i in range(len(l)-1, -1, -1):
        if l[i] > max:
            max = l[i]
        max_from_right.append(max)
    max_from_right = list(reversed(max_from_right))
    for i in range(len(l)):
        min_of_max.append(min(max_from_left[i], max_from_right[i]))
    res = 0
    for i in range(len(l)):
        res += min_of_max[i] - l[i]
    return res
print f([0,1,0,2,1,0,1,3,2,1,2,1])
