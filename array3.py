from array import *

# Example 1 – Basic slicing
arr1 = array('i', [10,20,30,40,50])
print(arr1[1:4])

# Example 2 – Start to index
arr2 = array('i', [10,20,30,40,50])
print(arr2[:3])

# Example 3 – Index to end
arr3 = array('i', [10,20,30,40,50])
print(arr3[2:])

# Example 4 – Step slicing
arr4 = array('i', [10,20,30,40,50,60,70,80])
print(arr4[::2])

# Example 5 – Reverse array
arr5 = array('i', [10,20,30,40,50])
print(arr5[::-1])