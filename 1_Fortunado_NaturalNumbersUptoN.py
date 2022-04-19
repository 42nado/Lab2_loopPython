#Write a PYTHON program to print the natural numbers up to n

numbers=int(input("Enter number :"))
print("List of natural number from 1 to ",numbers)

for x in range (numbers):
    print(x+1,end=", ")