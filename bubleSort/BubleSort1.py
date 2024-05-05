A = []
for i in range(0,5):
    A.append(int(input("Enter a number :")))




def bubleSort(A):
    n = len(A)
    for i in range (0,n - 1):
        for j in range (0 , (n -1) + 1):
            if (A[j] < A[j - 1]):
                A[j],A[j - 1] = A[j - 1],A[j]
    return A

sorted_A = bubleSort(A)
print(sorted_A)                
    
    


