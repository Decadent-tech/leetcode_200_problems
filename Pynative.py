import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
print(student_df)

# Define filter condition
filter = student_df['Marks'] > 80

student_df['Marks'].where(filter, other=0, inplace=True)
print(student_df)
# apply filter on dataframe
student_df_1 = student_df.filter(like='N', axis='columns')
print(student_df_1)
#rename column 'Marks' to 'Percentage'
student_df = student_df.rename(columns={'Marks': 'Percentage'})
print(student_df)
#####################################JOINING DATAFRAMES##########################################
import pandas as pd

# create dataframe from dict 
student_dict = {'Name': ['Joe', 'Nat'], 'Age': [20, 21]}
student_df = pd.DataFrame(student_dict)
print(student_df)

# create dataframe from dict 
marks_dict = {'Marks': [85.10, 77.80]}
marks_df = pd.DataFrame(marks_dict)
print(marks_df)

# join dfs
joined_df = student_df.join(marks_df)
print(joined_df)

##############################################GROUPING DATAFRAMES##########################################

import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Class': ['A', 'B', 'A'], 'Marks': [85.10, 77.80, 91.54]}
student_df = pd.DataFrame(student_dict)
print(student_df)

# apply group by 
student_df = student_df.groupby(['Class']).aggregate({'Marks': 'mean'}).reset_index()
print(student_df)
#################33List Exercises##############################
a=-1
b=3
print("a is greater than b" if a>b else"b is greater than a")

#swap first and last element of list
newList = [12, 35, 9, 56, 24]
print(newList)
newList[0], newList[-1] = newList[-1], newList[0]
print(newList)
print(len(newList))  # Length of the list

#######################reverse words in a string##########################
def reverse_words(input_string):
    words = input_string.split(' ')
    reversed_words = ' '.join(reversed(words))
    return reversed_words
input_string = input("Enter a string: ")
# Example input: "Hello World"
reversed_string = reverse_words(input_string)
print(reversed_string)  # Output: "World Hello"

#########################Check if a string is a palindrome##########################
def is_palindrome(input_string):
    # Remove spaces and convert to lowercase
    cleaned_string = ''.join(input_string.split()).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]
input_string = input("Enter a string: ")
 # List comprehension to filter words longer than 1 character
input_string_split = input_string.split()
even_words = [w for w in input_string_split if len(w)%2 ==0 ] 
print("Even words:", even_words)
print("Even words using filter:", " ".join(str(word) for word in even_words))
print("Palindrome" if is_palindrome(input_string) else "Not a palindrome")


########################3
s = "hello world"

# Use a list comprehension to create a new string by joining
# characters that are not 'o' from original string 's'
s = "".join([c for c in s if c != "o"])
print(s)

#############################
s = "amaama"

# Check palindrome using reversed()
pal = list(s) == list(reversed(s))

# Check symmetry
half = len(s) // 2
sym = s[:half] == s[half:] if len(s) % 2 == 0 else s[:half] == s[half+1:]

print("Symmetrical" if sym else "Not Symmetrical")
print("Palindrome" if pal else "Not Palindrome")