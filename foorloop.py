# 1. Print numbers from 1 to 5
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)


# 2. Print Hello 3 times
print("\nHello 3 times:")
for i in range(3):
    print("Hello")


# 3. Print list elements
print("\nList elements:")
numbers = [10, 20, 30, 40]
for n in numbers:
    print(n)


# 4. Print numbers from 1 to 10
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i)


# 5. Print even numbers from 1 to 20
print("\nEven numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 6. Print odd numbers from 1 to 15
print("\nOdd numbers from 1 to 15:")
for i in range(1, 16):
    if i % 2 != 0:
        print(i)


# 7. Print table of 5
print("\nTable of 5:")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)


# 8. Print characters of a string
print("\nCharacters of string:")
name = "Atmiyu"
for letter in name:
    print(letter)


# 9. Sum of numbers from 1 to 5
print("\nSum from 1 to 5:")
total = 0
for i in range(1, 6):
    total = total + i
print("Sum is:", total)
