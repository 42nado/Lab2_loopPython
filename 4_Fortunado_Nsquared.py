#Write a PYTHON program that prints       1 2 4 8 16 32 … n2

sequence=1
numbers=int(input("Enter number :"))
print("List of series :")
while(numbers):
    print(sequence, end =", ")
    sequence*=2
    numbers-=1