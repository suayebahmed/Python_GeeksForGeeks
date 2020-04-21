# one line factorial solving problem

def factorial(n):
    return 1 if (n == 1 or n == 0) else factorial(n - 1)

num = int(input("Enter a number for factorial: "))
factorial(num)

# iterative factorial

def fact(num):
    if  num == 1 or num == 0:
        return 1
    else:
        res = num * (num - 1)
        return res
x = 3
fact(x)
