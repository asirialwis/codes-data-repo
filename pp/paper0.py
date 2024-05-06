# n = int(input("Enter number for n : "))
# M = int(input("Enter number for M : "))


def multiply(M,n):
    if n == 1:
        return n
    else:
        return (M + multiply(M, n-1))
    

while (True):
    M = int(input("Enter value for M : "))
    if M == -1:
        break
    else:
        n = int(input("Enter Number for n : "))
        print(multiply(M,n))
