"""
Data Types :-

integer => 0, -1, 1, -2, 2, -3, 3, ...........
float => 3.12, 5.71, -8.91, 0.0, 3.0, -9.81, ..............
char => 'A', '=', 'k', '\', ')', 'M', ...........
string => "Word", "Hello", '1234', "123alphazero3.14",
Bool => True, False
"""

""" Input Statements """

# a = int(input("Enter the Number"))
#
# print(a + 1)

# Examples

# write a program to find the sum of n natural numbers
# given n value as an input to the program

# 1, 2, 3, 4, 5, 6, 7, 8
# Sum of N Natural Numbers = N * (N + 1) / 2

# N = int(input("Enter the Number"))
#
# answer = N * (N + 1) / 2
#
# print(answer)

# Area of Circle, Given Radius as Input

# Area of Circle = pie * (r ** 2)

# radius = float(input("Enter the Circle Radius"))
#
# Area = 3.14 * radius * radius
#
# print(Area)

# Simple Interest SI = P * T * R / 100

# principle = int(input("Enter the Principle"))
# time = float(input("Enter the time in years"))
# rate = float(input("Enter the rate"))
#
# simple_interest = (principle * time * rate) / 100
#
# print(simple_interest)

# write a program to compute no of seconds, ,minutes, hours, days in a year

# months_in_a_year = 12
# days_in_a_year = months_in_a_year * 30
# hours_in_a_year = days_in_a_year * 24
# minutes_in_a_year = hours_in_a_year * 60
# seconds_in_a_year = minutes_in_a_year * 60
#
# print("Months =", months_in_a_year)
# print("Days =", days_in_a_year)
# print("Hours =", hours_in_a_year)
# print("Minutes =", minutes_in_a_year)
# print("Seconds =", seconds_in_a_year)

# write a program to compute distance given speed and time

# train = 80 kmph
# distance = speed * time
#
# speed = int(input("Enter the speed"))
# time = int(input("Enter the time"))
#
# distance = speed * time
#
# print(distance)


# write a program to find the cost of fuel
# given mileage, distance, and cost of 1 litre fuel

# 50 km / lt , 200 kms, 100

# mileage = int(input("Enter the vehicle mileage"))
# distance = int(input("Enter the journey distance"))
# cost_of_litre_fuel = float(input("Enter the cost of litre fuel"))
#
# quantity = distance / mileage
# total_cost = quantity * cost_of_litre_fuel
#
# print(total_cost)


# write a program to find the (a - b)^2 / (a + b)^2 given a and b values

# a = int(input("Enter the a value"))
# b = int(input("Enter the b value"))
#
# answer = (a - b)**2 / (a + b)**2
#
# print(answer)

# write a program to find the no of persons in a country given,
# no of houses in a country and no of persons per house

# houses_count = int(input("Enter the houses count in a country"))
# persons_count = int(input("Enter the count of persons per house"))
#
# total_persons = houses_count * persons_count
#
# print(total_persons)

# write a program to find no of chocolates each person will get
# when the chocolates are equally distributed among the students,
# given no of students and no of chocolates

# students = int(input("Enter the students count"))
# chocolates = int(input("Enter the chocolates count"))
#
# answer = chocolates // students
#
# print(answer)


# a = 1
# b = 2

# a = a + 5 # a = 6
# b = b * 7 # b = 14
#
# a += 5 # a = a + 5
# b *= 7 # b = b * 7
# a -= 1 # a = a - 1
# b /= 3 # b = b / 3
# a //= 5 # a = a // 5
# a %= 11 # a = a % 11
#
# print(a)
# print(b)

# a, b = 2, 5
#
# a += b # a = a + b => a = 7, b = 5
# b -= a # b = b - a => b = -2, a = 7
# a *= (a-5) # => a = a * (a-5) => a = 14, b = -2
# b %= 3 # b = b % 3 => a = 14, b = 1
#
# print(a, b)

""" Conditional Statements """

# Program to find whether the given number is even or odd

# a = int(input("Enter the number"))

# if a%2 == 0:
#     print("Even")
# if a%2 != 0:
#     print("Odd")

# a = int(input("Enter the number"))
#
# if a%2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# a = int(input("Enter the number"))

# if a%2 == 1:
#     if a+1 == 2:
#         print("Hello")
#     else:
#         print("Hai")

# a = int(input("Enter the number"))
#
# if (a == 1 and a%2 ==1) or a%3 == 1:
#     print("Hello")


# a = int(input("Enter the Number"))
#
# if a%2 == 0:
#     print("Even Number")
#     print("----->")
#     print("OJSDUUJ")
# else:
#     print("Odd Number")
#     print("Gjbhvd")

# a = int(input("Enter the number"))
#
# if a == 1:
#     print("One")
# elif a == 2:
#     print("Two")
# elif a == 3:
#     print("Three")
# elif a == 0:
#     print("Zero")
# else:
#     print("Greater than 3")

# Examples on If statements

# Write a program to find whether the given number is +ve or -ve or zero

# a = int(input("Enter the number"))
#
# if a < 0:
#     print("-ve Number")
# elif a > 0:
#     print("+ve Number")
# else:
#     print("zero")


# a = int(input("Enter the Number"))
#
# if a == 3:
#     print("Hello")
# elif a%2 == 1:
#     print("Hai")
# else:
#     print("None of the above")

# name = input("Enter Your Name")
#
# if name == " ":
#     print("Not a valid Name")
# else:
#     print("Hello!!!", name)


# Write a program to check whether the given year is a Leap Year or not


# Leap Year Condition :- multiple of 400 or
# (multiple of 4 and not a multiple of 100)

# year = int(input("Enter the number"))
#
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# write a program to check voters eligibility for elections,
# given voters age in integer format

# age = int(input("Enter Your Age"))
#
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# write a program to find the largest one out of given two numbers?

# # Inputs
# number1 = int(input("Enter the first number"))
# number2 = int(input("Enter the second number"))
#
# # Logic
# if number1 > number2:
#     print(number1, "is the largest number")
# else:
#     print(number2, "is the largest number")

# grading system

# 91-100 => A
# 81-90 => B
# 71-80 => C
# 61-70 => D
# 51-60 => P
# <= 50 => F

# Inputs
# marks = int(input("Enter the marks"))
#
# # Logic
# if 91 <= marks <= 100:
#     print("A")
# elif 81 <= marks <= 90:
#     print("B")
# elif 71 <= marks <= 80:
#     print("C")
# elif 61 <= marks <= 70:
#     print("D")
# elif 51 <= marks <= 60:
#     print("P")
# elif 0 <= marks <= 50:
#     print("F")
# else:
#     print("Enter valid marks")

# print "high" when the temperature is greater than 45℃
# otherwise print "low",
# given the temperature as an input to the program

# # Inputs
# temperature = float(input("Enter the temperature"))
#
# #Logic
# if temperature > 45:
#     print("High")
# else:
#     print("Low")


# write a program to find the charge for the employee,
# given the work hours, cost per work hour, allowed hours of normal work.
# Consider rate for the extra work hours is 2 times the normal rate.

# hours = 12, rate = 100, company hours = 7, overtime = hours - company hours

# # Inputs
# hours = float(input("Enter the work hours"))
# rate = float(input("Enter the rate of each work hour"))
# company_hours = float(input("Enter the normal company allowed work hours"))
#
# #Logic
# if hours <= company_hours: # no overtime duty
#     charged_amount = rate * hours
#     print(charged_amount)
# else:
#     overtime = hours - company_hours
#     charged_amount = company_hours*rate + overtime * (2 * rate)
#     print(charged_amount)

# write a program to check whether the username and password
# given as inputs are valid or not?

# Inputs
# username = input("Enter the username")
# password = input("Enter the password")
#
# # Logic
# if username == "ROOT" and password == "ROOT@1729":
#     print("Correct Credentials")
# else:
#     print("Invalid Details")

# a = int(input("Enter the number"))

# print("Even" if a%2 == 0 else "Odd")
#
# b = "Hello" if a == 1 else "Hai"
#
# print(b)

""" Strings """

# a = "User1" + "User2" # "User1User2" String Concatenation
#
# print(a)

# a = "Word" * 3 # => "Word" + "Word" + "Word" => "WordWordWord"
# print(a)

# proposal = "Happy New Year\n"
# print(proposal * 10)

# name = "Hello"
#
# print(len(name))

""" Importing modules """

# import math
#
# print(math.floor(9.7))
# print(math.ceil(9.7))
# print(math.comb(5, 3))
# print(math.factorial(7)) # 1 * 2 * 3 * 4 * 5 * 6 * 7
# print(math.gcd(7, 14))
# print(math.lcm(12, 14))
# print(math.sqrt(7))
# print(math.exp(10)) # e^x
# print(math.pow(5, 7)) # 5 ** 7
# print(pow(2, 3, 5))
# print(math.remainder(13, 7)) # 13 % 7
# print(math.pi)
#
# pie = math.pi
#
# print(math.sin(pie/6))
# print(math.tan(pie/4))
# print(math.cos(pie/4))
#
# print(math.perm(5, 3))
# print(math.log(7, 10))
# print(math.fabs(-90))

# age1 = int(input("Friend"))
# age2 = int(input("Friend"))
# diff = age1 - age2
# print(abs(diff))

# import random

# print(random.randint(1, 10))
# print(random.uniform(1, 5))

""" Loops """

# for i in range(3):
#     print("hello")

# for i in range(100):
#     print(i)

# i = 0, i = 1, i = 2, i = 3, ......., i = 9, i = 10

# a = 1

# for i in range(10):
#     a = 2 * a
#     a = a - 1
#     a = a * 5
# print(a)


# for i in range(2, 10, 3): # start = 2, end = 10, step = 3
#     print(i)
# i = 2, i = 5, i = 8, i = 11

# for i in range(3, 7): # start = 3, end = 7, step = 1
#     print(i)
#
# for i in range(5): # start = 0, end = 5, step = 1
#     print(i)

# for i in range(3, 57, 9):
#     print(i)

# count = 0
#
# for i in range(1, 6):
#     count = count + i
#     print(i, count)
# i = 1, count = count + i => count = 0 + 1 => count = 1, print(1, 1)
# i = 2, count = count + i => count = 1 + 2 => count = 3, print(2, 3)
# i = 3, count = count + i => count = 3 + 3 => count = 6, print(3, 6)
# i = 4, count = count + i => count = 6 + 4 => count = 10, print(4, 10)
# i = 5, count = count + i => count = 10 + 5 => count = 15, print(5, 15)
# i = 6, terminates

# for i in range(1, 6):
#     print("i =", i)

# for i in range(1, 6):
#     print("i =", i, "i*i =", i*i)

# 2 Table

# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# 2 * 10 = 20

# Pattern => 2 * i = (2 * i) => if i = 7, 2 * 6 = 12

# for i in range(1, 11):
#     print("2 *", i, "=", 2*i)

# count = 0
#
# for i in range(1, 11): # i = 1 to 10
#     count = count + i
# print(count)

# n = int(input("Enter the N value"))
#
# for i in range(1, n+1):
#     print(i)


# n = int(input("Enter the N value"))
#
# count = 0
# for i in range(1, n+1):
#     count = count + i
# print(count)

# i = 5, 4, 3, 2, 1, 0
# for i in range(5, 0, -1): # start = 5, end = 0, step = -1
#     print(i)

# for i in range(100, 0, -1):
#     print(i)

# To print all the multiples of 5 between 1 and 100
# for i in range(1, 101):
#     if i % 5 == 0:
#         print(i)

# for year in range(1700, 2024):
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         print(year)

# 1 to 5
# count = 1
# for i in range(1, 8):
#     count = count * i
# print(count)

# count = 1
# i = 1, count = 1 * 1 = 1
# i = 2, count = 1 * 2 = 2
# i = 3, count = 2 * 3 = 6
# i = 4, count = 6 * 4 = 24
# i = 5, count = 24 * 5 = 120
# i = 6, terminates


# Factorial : factorial(5) = 1 * 2 * 3 * 4 * 5 = 120

# for i in range(1, 100):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)

# given a number, print all the factors of that number
# factors of 36 : 1, 2, 3, 4, 6, 9, 12, 18, 36

# get all numbers from 1 to 36 and check whether 36 is a multiple of those numbers

# n = int(input("Enter the Number"))
#
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)


# Count no of factors for 72

# 0 1 0 0 0 1 1 0 0 1 0 1

# count = 0
# for i in range(1, 37):
#     if 36 % i == 0:
#         count = count + 1
# print(count)

# Prime Number

# prime number : A number is prime if it has factors 1 and itself.
# No of Factors for Prime Number = 2
# Ex: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ............

# n = int(input("Enter the Number"))
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

# Write a program to find all the number between 1 and 1000 such that,
# that number should be a multiple of 3 and 5, but not 7

# for i in range(1, 1001):
#     if i%3 == 0 and i%5 == 0 and i%7 != 0:
#         print(i)


# Find all the Prime Factors of given Number

# N = int(input("Enter the Number"))
# for i in range(1, N + 1):
#     if N % i == 0:
#         n = i
#         count = 0
#         for j in range(1, n + 1):
#             if n % j == 0:
#                 count += 1
#         if count == 2:
#             print(i)

""" Patterns """

# *****
# *****
# *****
# *****
# *****

# for i in range(1, 6):
#     print("*"*5)

# *
# **
# ***
# ****
# *****

# for i in range(5, 0):
#     print("*" * i)

#     * => 4 spaces + 1 star => no of spaces = 5 - no of stars, no of stars = row number
#    ** => 3 spaces + 2 stars
#   *** => 2 spaces + 3 stars
#  **** => 1 spaces + 4 stars
# ***** => 0 spaces + 5 stars

# for i in range(1, 6):
#     print(" " * (5 - i), end='')
#     print("*" * i)

# ***** => row-1, 5-starts =>  no-of-stars = 6 - row-no
# **** => row-2, 4-starts
# *** => row-3, 3-starts
# ** => row-4, 2-starts
# * => row-5, 1-starts

# for i in range(1, 6):
#     print("*" * (6 - i))

# for i in range(5, 0, -1):
#     print("*" * i)

# A - 65, B - 66...., Z = 90, a - 97, b = 98, ...., z = 122

# ACE : 65 67 69

# print(ord('=')) # Char to ASCII Value
# print(chr(57)) #    ASCII Value to Char

# A => row no-1, 65 => 65 - 1 = 64 => char = 64 + row-no
# B => row no-2, 66 => 66 - 2 = 64
# C => row no-3, 67 => 67 - 3 = 64
# D => row no-4, 68 => 68 - 4 = 64
# E => row no-5, 69 => 69 - 5 = 64

# for i in range(1, 6):
#     print(chr(64 + i))

# A => 1, 65
# BB => 2, 66
# CCC => 3, 67
# DDDD => 4, 68
# EEEEE => 5, 69

# for i in range(1, 6):
#     print(chr(64+i) * i)


# A
# AB
# ABC
# ABCD
# ABCDE

# for i in range(1, 6):
#     for j in range(65, 65 + i):
#         print(chr(j), end='')
#     print()

# for i in range(65, 65 + 7):
#     print(chr(i))

# 1 * ----------->1
# 2 *** ---------->3
# 3 ***** --------->5
# 4 ******* -------->7
# 5 ********* ------->9

# for i in range(1, 6):
#     print("*" * (2*i-1))

# 1 1
# 2 22
# 3 333
# 4 4444
# 5 55555

# for i in range(1, 6):
#     print(str(i) * i)

# 1 1
# 2 12
# 3 123
# 4 1234
# 5 12345

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

""" Break Statement """

# for i in range(1, 11):
#     print(i)
#     if i == 6:
#         break

""" Continue """

# for i in range(1, 6):
#     if i%2 == 1:
#         continue
#     print(i)
#     print("Hello")
#     print("HAI")


""" While Loop """

# a = 1
# while a + 1 == 2:
#     print("Hello")
#     a = a + 1
#     print(a)

# a = 1
#
# while a < 6:
#     print(a)
#     a = a + 2
# print("Hello")

""" While Loop Examples """

# Print all the numbers from 1 to 10

# i = 1 # initialization (start)
# while i < 4: # Condition (Stop)
#     print(i)
#     i = i + 2 # Increment (Step)
# #
# for i in range(1, 4, 2):
#     print(i)


# while (Stomach is not full):
#     Eat 1 Idly

# for i in range(1, 20):
#     Eat 1 Idly

# print all the even numbers from 1 to 100

# for i in range(1, 101):
#     if i%2 == 0:
#         print(i)

# i = 1
# while i < 101:
#     if i % 2 == 1:
#         print(i)
#     i = i + 1

# n = int(input("Enter the Number"))
# i = 1
# while i < (n+1):
#     if i % 2 == 1:
#         print(i)
#     i = i + 1

# To find the sum of the digits in a number
# Ex: 123 => 1 + 2 + 3 = 6
# Ex: 982 => 9 + 8 + 2 = 19

# a = 12

# print(a % 10) # To find the last digit
# print(a // 10) # To find the number excluding last digit

# a = int(input("Enter the Number"))
# count = 0
#
# while a > 0:
#     lastDigit = a % 10 # To find the last digit
#     count = count + lastDigit # add that last digit to count
#     a = a // 10 # to remove the last digit
# print(count)

# 1 => 12345, count = 5
# 2 => 1234, count = 9
# 3 => 123, count = 12
# 4 => 12, count = 14
# 5 => 1, count = 15
# 6 => 0

# n = 1835
# count = 0
# while n > 0:
#     lastDigit = n % 10
#     count += lastDigit
#     n = n // 10
# print(count)

# To check whether the sum of given number is equal to a given number or not

# n = int(input("Enter the Number"))
# target = int(input("Enter the Target"))
#
# count = 0
# while n > 0:
#     lastDigit = n % 10
#     count += lastDigit
#     n = n // 10
# if count == target:
#     print("Equal")
# else:
#     print("not Equal")

# Armstrong Number (100 to 999)

# 371 => 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371

# n = int(input("Enter the Number"))
# target = n
#
# count = 0
# while n > 0:
#     lastDigit = n % 10
#     count = count + lastDigit ** 3
#     n = n // 10
#
# if count == target:
#     print("ArmStrong Number")
# else:
#     print("Not an ArmStrong Number")


# import math
# n = int(input("Enter the Number"))
# target = n
#
# count = 0
# while n > 0:
#     lastDigit = n % 10
#     count = count + math.factorial(lastDigit)
#     n = n // 10
#
# if count == target:
#     print("Strong Number")
# else:
#     print("Not a Strong Number")

# n = int(input("Enter the Number"))
#
# reverseNumber = 0
#
# while n > 0:
#     lastDigit = n % 10
#     reverseNumber = reverseNumber * 10 + lastDigit
#     n = n // 10
# print(reverseNumber)

# palindromes => noon, malayalam, racecar, level, mom

# to find whether given number is a palindrome or not

# Ex: 13931 => palindrome
# Ex: 123 => Not Palindrome

# n = int(input("Enter the Number"))
# originalNumber = n
# reverseNumber = 0
#
# while n > 0:
#     lastDigit = n % 10
#     reverseNumber = reverseNumber * 10 + lastDigit
#     n = n // 10
# if reverseNumber == originalNumber:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

""" Lists """

# a = 1
# b = 2
# greet = "Hello"
# pie = 3.14

# l = [1, 2, "Hello", 3.14]
# print(l)
# print(*l)

# l = [1, 2, "Hello", 3.14]
# print(l)
# l.append("Hai")
# print(l)

# l = [1, 2, "Hello", 3.14]
# print(l)
# l.insert(1, "Hai")
# print(l)

# l = [1, 2, "Hello", 3.14]
# print(l)
# l.pop(2)
# print(l)

# l = [123, 1, 2, 123, "Hello", 3.14, 123]
# print(l)
# l.remove(123)
# print(l)

# l = [1, 2, "Hello", 3.14]
# print(l)
# l[1] = l[1] + 2
# print(l)

# l = [1, 2, "Hello", 3.14, 9]
# print(len(l))

# l = [1, 2, "Hello", 3.14, 1, 2, 2]
# print(l.count(3))

# l = [1, 2, "Hello", 3.14]
# print(l.index(3.14))

# l = [1, 2, "Hello", 3.14]
#
# for i in range(0, 4):
#     print("Index =", i, "Value =",l[i])

# l = [2, 0]
# for i in l:
#     print(i)

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in l:
#     print(*i)

# l = list(map(int, input("Enter numbers with space seperation").split()))
# print(l)


""" Sets """

# l = {1, 3, 5}
#
# l.add(12)
#
# print(l)

# l1 = {1, 3, 5}
# l2 =  {3, 6, 7}
#
# print(l1.intersection(l2))

""" Tuple """

# l1 = (3, 4, 5, 3, 4, 3, 3, 3)
#
# l1 = l1 + (8,0)
#
# print(l1.count(3))

""" F-String """

# a = 1
# b = 2
#
# print(f"a = {a * 2}, b = {b + 7}")

""" Dictionary """

# l = {"red":1, "green":2, "blue":5} # key :  value
#
# l.update({"purple": 7})
#
# print(l)

# l = {"red":1, "green":2, "blue":5} # key :  value

# [('red', 1), ('green', 2), ]

# print(l.get("orange"))

# from collections import defaultdict
#
# d = defaultdict(int)
# l = [1, 4, 2, 5, 3, 2 ,0, 9,  7, 6, 3]

# ele : count

# for i in l:
#     d[i] = d[i] + 1
# print(d)

""" Functions or Methods"""

# N = int(input())
#
# for i in range(1, N + 1):
#     if N % i == 0:
#         count = 0
#         for j in range(1, i +1):
#             if i % j == 0:
#                 count = count + 1
#         if count == 2:
#             print(i)
#
# def checkPrime(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count = count + 1
#
#     if count == 2:
#         return "Prime Number"
#     else:
#         return "Not a Prime Number"
#
#
# print(checkPrime(19))

# def Add(a, b):
#     return a + b
#
# print(1 + 2)
# print(4 + 6)
#
# def checkLeapYear(year):
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         return "Leap Year"
#     else:
#         return "Not a Leap Year"

# print(checkLeapYear(2019))
# print(checkLeapYear(2032))
# print(checkLeapYear(2023))
# print(checkLeapYear(2190))
# print(checkLeapYear(1700))

""" Slicing """
# l = [2, 5, 6, 9, 8, 1, 0]
#
# print(l[::-2])

""" Class """

# class Person:
#     name = ""
#     Age = 0
#
# p1 = Person()
# p2 = Person()
#
# p1.name = "Pawan Kalyan"
# p1.Age = 21
#
# p2.name = "Samara Simha Reddy"
# p2.Age = 22
#
#
# class Person:
#     name = ""
#     Age = 0
#     def __init__(self, NAME, AGE):
#         self.name = NAME
#         self.Age = AGE
#
# p1 = Person("Hello", 12)
# p2 = Person("Hai", 21)
# p3 = Person("Bye", 34)
#
# class Person:
#     name = "word"
#     Age = 0
#
# p1 = Person()
#
# del p1 # delete p1 object
#
# class Person:
#     name = "Hello"
#     Age = 21
#
#     def __str__(self):
#         return "Copy of Person Class"
#
# p = Person()
#
# print(p)
#
#
# # OOPS => Encapsulation, Polymorphism, Inheritance, Abstraction
#
# class Employee:
#     id = 9434
#     salary = 122
#     designation = "developer"
#
""" File Handling """
#
# file = open('temp.txt', 'r')
#
# l = file.read().split("\n") # "Line1\nLine2\nLine3\n....."
# print(l)
#
""" Sorting """
#
# l = [3, 0, 1, 7, -1]
#
# l.sort()  # Sorts the list
#
# print(l)
#
""" List Comprehension """
#
# l = [i*i for i in range(1, 11)]
#
# print(l)
#
# l = [i if i % 2 == 0 else 0 for i in range(1, 21)]
#
# print(l)
#
""" Exceptional Handling """
#
# try:
#     print(1)
# except:
#     print("Error occured")
#
# print("Hello")
#
# a = input()
# try:
#     a = a + 1
# except:
#     print("Error Occured")
#
# print("hELLO")
# print("Hai")
#
# try:
#     l = [1, 2, 3]
#     print(l[11])
#     print("No error")
# except ZeroDivisionError:
#     print("Zero Division Error")
# except NameError:
#     print("Name Error")
# except IndexError:
#     print("Index Error")
#
# a = int(input())
# b = int(input())
# try:
#     c = a // b
# except:
#     print("Error Occured")
# else:
#     print(c)
# finally:
#     print("Last Block")
#
#
""" DateTime """
#
# import datetime
#
# current = datetime.datetime(2023, 5, 26)
#
# print("Current Time =", current)
#
# delta = datetime.timedelta(weeks=1, days=234)
#
# final = current + delta
#
# print(final)
#
""" Lambda Function """
#
# square = lambda x : x * x
#
# print(square(5))
# print(square(45))
# print(square(29))
#
""" Map """
#
# def square(n):
#     return n * n
#
# l = list(map(square, [2, 3, 4, 1, 7]))
#
# print(l)
#
# l = [2, 3, 4, 1, 7]
#
# l = list(map(lambda x : x * x, l))
#
# print(l)
#
""" Filter """
#
# l = list(filter(lambda x : x%2 == 0, [2, 5, 0, 1, 5, 7, 9]))
#
# print(l)
#
""" Frozen Sets """
#
# fs1 = frozenset([7, 9, 1])
# fs2 = frozenset([1, 2, 3, 7])
#
# print(fs2.difference(fs1))
#
""" Reduce """
#
# from functools import reduce
#
# ans = reduce(lambda x, y : 0 if x > y else 1 , [1, 2, 3, 4, 5])
#
# print(ans)
#
""" Sleep """
#
# import time
#
# print("Hello")
#
# time.sleep(3) # waits for 3 seconds
#
# print("Hai")
#
""" Threads """
#
# import threading
# import time
#
# def fun(id, sec):
#     time.sleep(sec)
#     print("Exam", id, "Done")
#
# threads = []
#
# for i in range(1, 6):
#     thread = threading.Thread(target=fun, args=[i, 6-i])
#     threads.append(thread)
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
""" API Requests """
#
# import requests
#
# response = requests.get("http://worldtimeapi.org/api/timezone/Australia/Sydney")
#
# print(response.json())
#
#
""" Generator Function """
#
# def fun(n):
#     for i in range(1, n +1):
#         yield i
#
# l = fun(3)
#
# print(next(l))
# print(next(l))
# print(next(l))
#
""" Regular Expressions """
#
# import re
#
# s = "Jeff Bezos email id is jeff@gmail.com and Bezos1@yahoo.ind"
#
# result = re.findall(r'[A-Za-z0-9]+@[a-z]{5}.[a-z]{3}', s)
#
# print(result)
#
# s = "https://www.Amazonjdjhhduhh.org, Jeff Bezos website link is https://www.Amazon.in, https://www.Amazon1232323.com"
#
# result = re.findall(r'https://www.[A-Za-z0-9]+.[A-Za-z0-9]+', s)
#
# print(result)
#
# s = "HelloHaiHello"
#
# new = re.sub('H', '', s)
#
# print(new)
#
# s = "Hello 123 Hai 456 Bye 789"
#
# result = re.sub(r'[0-9]', '', s)
#
# print(result)
#
""" Strings """
#
# s = "Hello"
# print(s[1])
# for i in s:
#     print(i)
#
""" Fibonacci Sequence """
#
# # 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# first = 0
# second = 1
# for i in range(1, 23):
#     result = first + second
#     first, second = second, result
#     print(result)
#
""" Random Number Guessing Game"""
#
# import random
#
# while True:
#     guessedNumber = int(input("Guess the Number"))
#     randomNumber = random.randint(1, 6)
#     if guessedNumber == randomNumber:
#         print("You Won")
#     else:
#         print(f"You Lose, Random Number = {randomNumber}")
#     response = input("Do You Wanna Play Again (yes / no)")
#     if response == 'no':
#         break
#
""" Importing own modules"""
#
# from mymodule import factorial, Person
#
# print(factorial(8))
#
# p = Person()
#
# print(p.name, p.age)
#
""" Caesar Cipher """
#
# # "Hello" + 1 =>  "Ifmmp"
# # "ABc" + 5 => "FGI"
#
# s = input("Enter the String")
# key = int(input("Enter the Key")) % 26
#
# print(f"Input String = {s}")
# encryptedString = ''
#
# for letter in s:
#     oldLetterASCIIValue = ord(letter)
#     newLetterASCIIValue = oldLetterASCIIValue + key
#     newLetter = chr(newLetterASCIIValue)
#     encryptedString = encryptedString + newLetter
#
# print(f"Encrypted String = {encryptedString}")
