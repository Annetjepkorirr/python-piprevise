#  Write a Python program to get a single string from two given strings, separated by a space,
#  and swap the first two characters of each string

name1 = "Hooper"
name2 ="lab"

name1_word = name1[:2]+name2[2:]
name2_word = name2[:2]+name1[2:]

combined_word = name1_word + " " + name2_word
print(combined_word)


#  Write a Python function that takes a list of words and returns the longest word and 
#  the length of the longest one
def find_longest_word(words):
    max_length = 0
    longest_word = " "
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word (word)
    return max_length

# Write a Python program that accepts a comma-separated sequence of words as input and prints the 
# distinct words in sorted form (alphanumerically).  
def series_of_words(letters):
    letters = [stmt(i) for i in letters]
    letters.sort()
    letters = [num(i) if i.isdigit() else i for i in letters]
    return letters
           
#  Write a Python function that takes two lists and returns True if they have at least one common member.
def common_numbers(list1,list2):
    for num in list1:
        if num in list2:
            return True
        else:
            return False    
        
# Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"] ["#000000", "#FF0000", "#800000", "#FFFF00"]
colours = ["Balck","Red","Maroon","Yellow"]
convert_word =[]

for color in colours:
    color_dict = {"color":color}
    convert_word.append(color_dict)
    
print(convert_word)    

# Write a Python program to check whether all dictionaries in a list are empty or not
list_of_dicts = [{},{}]
for dicts in list_of_dicts:
    if len(dicts) == 0:
        print("is empty")
    else:
        print("not empty")


# Given a list of numbers, use list comprehension to remove all odd numbers from the list:
numbers = [3,5,45,97,32,22,10,19,39,43]
remove_odd_numbers =[nums for nums in numbers if num%2 == 0]
print(remove_odd_numbers)


# Find the common numbers in two lists (without using a tuple or set) 
list_a = 1, 2, 3, 4, 
list_b = 2, 3, 4, 5
common_number = []
for num in list_a:
    if num in list_b:
        common_number.append(num)
        
    print(common_number)    

# Write a Python function to remove all vowels in a string  
def removeVowels(words):
    vowels  = "aeiouAEIOU"
    emptyWord = ""
    for word in words:
        if word not in vowels:
            emptyWord+=word
            
        return emptyWord    