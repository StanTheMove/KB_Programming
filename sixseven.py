import math 
a = int(input("Enter a(from 1 - 1000): "))
b = int(input("Enter b(from 1 - 1000): "))
if(a or b > 1000 or a or b < 1):
    print("Error")

print ("a + b =", a + b)
print ("Max =", max(a, b))
