# Write a function that takes an unknown number of arguments and returns their sum.
def find_sum_of_num(*args):
    return sum(args)
print(find_sum_of_num(23,11,34,12))

# Write a function that takes two arguments, the first being a string and the second being 
# an unknown number of integers. The function should return a new string where the integers have
# been added to the original string.
def name_and_number(names,*args):
    return names + "" .join(nm(i) for i in args)

print(name_and_number("I am a student,45"))

# Write a function that takes an unknown number of keyword arguments and returns a 
# dictionary where the keys are the argument names and the values are the argument values.
def unknown_numbers(**kwargs):
    return kwargs

print(unknown_numbers(name = "student", age =10))

# Write a function that takes a function and an unknown number of arguments, and returns 
# the result of calling the function with the arguments.
def nums(function,*args):
    return function(args)

# Write a function that takes a list of integers and an unknown number of keyword arguments. 
# The function should return a new list where each integer in the original list has been multiplied 
# # by the value of the corresponding keyword argument.

# def list_of_intergers(numss,**kwargs):
#     new_list =[]
#     for num in numss:
#         product = num
#     for key,value in kwargs.items():

# Write a function that takes a list of integers and an unknown number of additional integers 
# as arguments. The function should return the index of the first occurrence of the sum of the list 
# and the additional integers

# def take_list_numbers(int,**args):
    

# Write a function that takes an unknown number of keyword arguments, each with a string value. 
# The function should concatenate all the strings and return the resulting string
def unkown_num(**kwargs):
     return "".join(kwargs.values())
 
print(unkown_num(i ="I am ",q="a", w="student"))