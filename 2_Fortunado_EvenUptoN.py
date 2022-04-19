#Write a PYTHON program to print even numbers up to n

numbers=int(input("Enter number :"))
print("List of Even number between 1 and ",numbers)
for x in range(1,numbers+1):
    if x%2==0:
      print(x,end=", ")