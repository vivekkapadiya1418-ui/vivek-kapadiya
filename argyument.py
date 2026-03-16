"""#calling function
def simple_interest(p, t, r):
    si = (p * t * r) / 100
    print("Simple Interest:", si)

# calling function
simple_interest(p=10000, t=2.5, r=3.5)"""

#sqare or number
def sqr(num, exp=2):
    return num ** exp

print(sqr(3))      
print(sqr(3,3))    
print(sqr(2,4))

"""#default argyument
def greet(name="Guest"):
    print("Hello", name)

greet("Alice")
greet()"""

"""#another example
def add(a, b=5):
    print("Sum:", a + b)

add(10,20)
add(10)"""

"""#variable name argyument
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(10,20))
print(add_numbers(5,10,15,20))"""

"""#using built function
x = [1,2,3,4,5]

print("Length:", len(x))
print("Sum:", sum(x))
print("Maximum:", max(x))
print("Minimum:", min(x))
print("Type:", type(x))"""

