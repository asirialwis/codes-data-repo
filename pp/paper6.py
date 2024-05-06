

def sumcube(n):
    if n == 1:
        return 1
    else:
        return (sumcube(n-1) + n * n * n)
    

while(True):
    n = int(input("Enter Integer for cube"))
    if n < 0:
        print("Its not an Int value")
        break
    else:
        result = sumcube(n)
        print(result)
