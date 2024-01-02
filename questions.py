#You will be turning in this assignment to your Google classroom. Please save your 5 functions to one .py file and demark the question numbers and the question in a comment above its respective function.

#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):

    print(f"Hello_{user_name}!")

#testcase :
user_input = input("Enter your username: ")
print (hello_name(user_input))

               
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():

    for number in range(1, 100, 2):
        print(number)

#testcase
first_odds()

               
#Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    
    if not a_list:
        return None  # Return None for an empty list

    max_number = a_list[0]  # Assume the first number is the maximum

    for num in a_list:
        if num > max_number:
            max_number = num  # Update max_number if a larger number is found

    return max_number

# testcase:
numbers = [4, 101, 12, 18, 17]
numbers1=[]
result = max_num_in_list(numbers1)
print(f"The maximum number in the list is: {result}")
               
#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
  
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False

# testcase:
year_to_check = 2021
result = is_leap_year(year_to_check)
print(f"Is {year_to_check} a leap year? {result}")

               
# #Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    
    if not a_list or len(a_list) < 2:
        return False  # An empty list or a list with one element is considered non-consecutive

    sorted_list = sorted(a_list)

    for i in range(len(sorted_list) - 1):
        if sorted_list[i] + 1 != sorted_list[i + 1]:
            return False

    return True

# testcase:
consecutive_list = [2, 3, 4, 5, 6, 7]
non_consecutive_list = [1, 2, 4, 5]

result_consecutive = is_consecutive(consecutive_list)
result_non_consecutive = is_consecutive(non_consecutive_list)

print(f"Is {consecutive_list} consecutive? {result_consecutive}")
print(f"Is {non_consecutive_list} consecutive? {result_non_consecutive}")
