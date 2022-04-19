#Write a PYTHON program to sum the given sequence 1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!

num=int(input("Enter number:"))
sum = 0
fact = 1
for i in range(1, num + 1):
    # Update factorial
    fact *= i
    # Update series sum
    sum += 1.0 / fact
    if i != num:
        print("1/",i,"! + ", end=" ")
    else:
        print("1/",i,"! =", end=" ")
print(sum)