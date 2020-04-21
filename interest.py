# Simple interest formula is given by:
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate

principle = int(input("What is your principle amount? : "))
time = int(input("Enter total time. :"))
rate = int(input("what is the interest rate? : "))

total_interest = int((principle  * time * rate) / 100)

print(total_interest)
