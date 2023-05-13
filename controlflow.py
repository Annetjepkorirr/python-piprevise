# Write a Python program that takes a list of strings as input and outputs
# the number of times each string appears in the list, using a dictionary and 
# conditional statements.
def get_names(names):
    empty ={}
    for name in names:
        if name in empty:
            empty[name]+=1
        else:
            empty[name] =1   

# Write a Python program that takes a list of numbers as input and outputs the median
# of the numbers 

nums =[7,1,4,5,7]    
get_number = sorted(nums)

l =len(get_number)
middle =l //2
if l%2 == 0:
    median =(get_number[middle -1]+ get_number)/2
else:
    median = get_number[middle]

# Write a Python program that takes a list of numbers as input and outputs the second largest 
# number in the list using conditional statements and a for loop.
# def find_second_largest_number(numbers):
#     large_number = 0
#     second_number = 0
#     for num in numbers:
#         if large_number is 0:
#             large_number = num
#             continue
#         if num > large_number:
#             second_number = large_number
 

de
    
# Write a Python program that takes a year as input and determines if it is a leap year.
def find_leap_year(years):
    for year in years:
        if year %4 != 0:
            return False


# Write a Python program that takes a string as input and checks if it is a palindrome 
# (reads the same forwards and backwards), ignoring spaces and punctuation.
def palindrome(word):
    word1 = word[::-1]
    if word1 == word:
        print(f"palindrome")
    else:
        print(f"not palindrome")    