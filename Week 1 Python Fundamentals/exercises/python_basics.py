# Python Basics Practice

# Addition Calculator
a = 10
b = 20
print("Addition:", a + b)

# Even or Odd
num = 7

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Multiplication Table
number = 5
print("\nMultiplication Table of", number)

for i in range(1,11):
    print(number, "x", i, "=", number*i)

# Find largest number
numbers = [10, 45, 32, 67, 89]

largest = max(numbers)

print("\nLargest Number:", largest)

# Average calculation
total = sum(numbers)
average = total / len(numbers)

print("Average:", average)