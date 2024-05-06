


def power(x , n):
    if( n == 0):
        return 1
    else:
        return x * power(x, n -1)
    
while(True):
    n = int(input("Enter value for Exp : "))
    if( n < 0):
        break
    else:
        x = int(input("Enter value for Base : "))
        print(power(x,n))
