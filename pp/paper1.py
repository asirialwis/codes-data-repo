#Fibonacci Question
#n = int(input("Enter Fibonacci Number"))


def Fibbonacci(n):
    if n <= 1:
        return n
    else:
        return Fibbonacci(n - 1) + Fibbonacci(n - 2) 

#while loop

while(True):
    n=  int(input("Enter Fibonacci Number"))
    if n == -1:
        break
    else:
        result = Fibbonacci(n)
        print(result)