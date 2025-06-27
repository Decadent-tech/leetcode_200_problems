import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
# before rename
print(student_df)

#rename marks as percentage
student_df.rename(columns={"marks":"perce."},inplace=True)
# after rename
print(student_df)

#student_df.rename(columns={"name":"NAME","age":"AGE","perce.":"PERCENTAGE%"},inplace=True)
# after rename
#print(student_df)

print(student_df.columns)

student_df.rename(columns=lambda x: x.upper(), inplace=True)
# after rename with lambda
print(student_df)

student_df.rename(columns={"NAME": "#NAME", "AGE": "#AGE", "PERCE.": "#PERCENTAGE%"}, inplace=True)
# after rename with dict
print(student_df)

student_df.rename(columns=lambda x: x[1:], inplace=True)
# after rename with lambda to remove first character
print(student_df)

student_df.rename(columns= str.lower, inplace=True)
# after rename with str.lower
print(student_df)

#using indexing to rename

student_df.rename(columns={student_df.columns[2]:'PERC'},inplace=True)
# after rename with column index
print(student_df)

# using unknown columns name 

#student_df.rename(columns={'xsdcfdffgf':'AGE'}, inplace=True, errors='raise')
# This will raise an error because 'xsdcfdffgf' does not exist in the
#print(student_df)

# using 


student_df=student_df.set_axis(['new_name','new_age','new_marks'],axis='columns')
# after set_axis
print(student_df)


col = pd.MultiIndex.from_arrays([['Class A', 'Class A', 'Class B', 'Class B'],
                                 ['Name', 'Marks', 'Name', 'Marks']])
student_df = pd.DataFrame([['Joe', '85.10', 'Nat', '77.80'], ['Harry', '91.54', 'Sam', '68.55']], columns=col)
print(student_df)

student_df = student_df.rename(columns=str.upper, level=1)
print(student_df)