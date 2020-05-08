a = input("Enter a string: ")

if a.lower() == a[::-1].lower():
    print ("palindrome")
else: 
    print("not pallindrome")
