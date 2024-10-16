# Python Interview Coding Questions
# Question 1: Write a Python program to check if a string is a palindrome.
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


name = "deed"
if is_palindrome(name):
    print(f"{name} is a palindrome.")
else:
    print((f"{name} is not a palindrome."))

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("enter a string: ")
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print((f"{input_string} is not a palindrome."))

name = "usman"
a = ''.join(reversed(name))

print(a)

# Question 2: Write a Python program to find the factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
number = 5
result = factorial(number)
print(result)

import math

num = int(input("enter a number: "))

if num < 0:
    print("factorial is not defined")
else:
    print(f"the factorial of {num} is {math.factorial(num)}")
    
# Question 3: Write a Python program to find the largest element in a list.

list = [1,2,3,4,5]
m = max(list)
print(m)

numbers = input("enter numbers sperated by space.")

number_list = [int(num) for num in numbers.split()]

largest = number_list[0] if number_list else None
for num in number_list:
    if num > largest:
        largest = num
        print(largest)

if largest is not None:
    print(f"the largest element in the list is: {largest}")
else:
    print("the list is empty.")

# Question 4: Write a Python program to reverse a string.

name = "usman"
reverse_name = "".join(reversed(name))

print(reverse_name)

# Question 5: Write a Python program to count the frequency of each element in a list.

numbers = input("enter numbers separated by space: ")

num_list = [int(num) for num in numbers.split()]

for n in set(num_list):
    print(f"{n}: {num_list.count(n)}")

# Question 6: Write a Python program to check if a number is prime.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("enter a number: "))

if is_prime(number):
    print(f"{number} is a prime")
else:
    print("Not a prime")

# Question 7: Write a Python program to find the common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 2, 7, 4, 5]

a = []
for i in list1:
    for j in list2:
        if i == j:
            a.append(i)

print(a)

common_elements = list(set(list1) & set(list2))

print(common_elements)

# Question 8: Write a Python program to sort a list of elements using the bubble sort algorithm.

list1 = [5, 2, 9, 1, 6, 4]
for i in range(len(list1)):
    for j in range(len(list1) -1):
        if list1[j] > list1[j +1]
        list1[j], list1[j + 1]
    