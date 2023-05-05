# Write a Python function that takes two arguments (a and b) and returns their sum.
def add_nums(a,b):
    answer = a+b
    return answer

# Write a Python function that takes a string as input and returns the string reversed.
def reverse_str(word):
    return word[::-1]

# Write a Python function that takes a list of integers as input and returns the sum
#  of all the integers in the list.    
def list_of_intergers(nums):
    summation =0
    for num in nums:
        summation+=num
    return summation

# Write a Python function that takes a list of integers as input and returns a new list 
# with all the even numbers removed.
def list_intergers(num_word):
    empty_arr =[]
    for x in num_word:
        if x%2 !=0:
            empty_arr.append(x)
    return empty_arr        
            
# Write a Python function that takes a list of integers as input and
# returns the highest value in the list.  
def highest_number(number):
    y =max(number)
    return y
print(highest_number([5,7,11,34]))


# Write a Python function that takes a list of strings as input and returns a new list 
# with all the strings capitalized. 
         
def capitalise_str(words):
    add_empty =[]
    for word in words:
        add_empty.append(word.capitalize())
    return add_empty
# print(capitalise_str(["mary","jane"]))


   
  
    