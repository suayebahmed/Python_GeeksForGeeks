import random

a =[]
b = []

for i in range(40):
    i = random.randint(1, 40)
    a.append(i)
    
for i in range(40):
    i = random.randint(1,40)
    b.append(i)

x = []

for i in a:
    if i in b:
        x.append(i)
        
y = sorted(list(dict.fromkeys(x)))

print(y)
