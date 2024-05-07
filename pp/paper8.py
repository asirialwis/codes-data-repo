
def sum(n):
    if n == 1:
        return  1
    else:
        return sum(n-1) + n
    
while(True):
    n = int(input("Enter Number"))
    if n == -1 :
        print("Number should be positive")
        break
    elif n <= -1:
        print("Enter positive numbers only")
        continue
    else:
        result = sum(n)
        print(result)
