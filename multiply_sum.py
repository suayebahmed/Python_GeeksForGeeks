   """
   Accept two integer numbers from 
   a user and return their product 
   and if the product is greater than 
   1000,then return their sum
   """

def result(x, y):
    if x * y <= 1000:
        return x * y
    else:
        return x + y
        
x = float(input("X:"))
y = float(input("Y:"))

print(result(x, y))
