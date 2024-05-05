A = []

for  i in range(5):
    A.append(int(input("Enter the Number :")))

def partiotion(A,p,r):
    x = A[r]
    i = p -1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i + 1],A[r] = A[r],A[i + 1]
    return i + 1        

#p = 0
#r = len(A) - 1
#partiotion(A,p,r)
#print(A)

def quickSort(A,p,r):
    if p < r:
        q = partiotion(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q + 1 , r)

quickSort(A,0,len(A)-1)
print(A)        




#-----------common Pseudo code-----------

# procedure quickSort(A, p, r)
#    if p < r then
#       q = partition(A, p, r)
#       quickSort(A, p, q-1)
#       quickSort(A, q+1, r)
#    end if
# end procedure

# procedure partition(A, p, r)
#    x = A[r]
#    i = p - 1
#    for j = p to r - 1 do
#       if A[j] <= x then
#          i = i + 1
#          swap A[i] and A[j]
#       end if
#    end for
#    swap A[i+1] and A[r]
#    return i + 1
# end procedure