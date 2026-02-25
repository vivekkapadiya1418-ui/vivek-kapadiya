# 1) Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

print("------------")

# 2) Print odd numbers between 1 to 20
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

print("------------")

# 3) Print table of 4
num = 4
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

print("------------")

# 4) Print reverse numbers (10 to 1)
i = 10
while i >= 1:
    print(i)
    i -= 1

print("------------")

# 5) Find largest number in list
numbers = [10, 45, 23, 67, 12]
largest = numbers[0]
i = 1

while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1

print("Largest number is:", largest)

print("------------")

# 6) Print even numbers between 1 to 20
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
    
# 7) Sum of numbers taken from user

total = 0
n = int(input("How many numbers you want to add: "))

i = 1
while i <= n:
    num = int(input("Enter number: "))
    total += num
    i += 1

print("Sum =", total)
    
 
  
    
    