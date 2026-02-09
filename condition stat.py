# Input for age, marks, and number for odd/even
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
num = int(input("Enter a number: "))

# Check voting eligibility
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

# Check marks and grade
if marks >= 90:
    print("You will get A grade")
elif marks >= 70:
    print("You will get B grade")
else:
    print("You will get C grade")

# Check if the number is odd or even
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
