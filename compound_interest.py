#Compound Interest = P(1 + R/100)**t
#Where,
#P is principle amount
#R is the rate and
#T is the time span

p = float(input("principle amount: \n--->> "))
r = float(input("rate: \n--->>"))
t = float(input("time: \n--->>"))

result = p * (1 + (r / 100)) ** t

print("compound is: ", int(result))
