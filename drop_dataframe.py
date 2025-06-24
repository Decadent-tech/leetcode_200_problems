import pandas as pd

student_dict = {"name": ["Joe", "Nat"], 
                "age": [20, 21], 
                "marks": [85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)
print(student_df.drop(columns=student_df.columns[-1], inplace=True))  # Drop columns 'age' and 'marks' from DataFrame
print(student_df)  # Display the DataFrame after dropping columns

student_dict = {"name": ["Joe", "Nat"], 
                "age": [20, 21], 
                "marks": [85.10, 77.80], 
                "class": ["A", "B"],
                "city": ["London", "Zurich"]
                }
# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)
print(student_df.drop(columns=student_df.iloc[:, range(2)], inplace=True))
print(student_df)  # Drop columns '

print("################function to drop columns from DataFrame")

col = pd.MultiIndex.from_arrays([['Class A', 'Class A', 'Class B', 'Class B'],
                                 ['Name', 'Marks', 'Name', 'Marks']])
# create dataframe from 2darray
student_df = pd.DataFrame([['Joe', '85.10', 'Nat', '77.80'], 
                           ['Harry', '91.54', 'Sam', '68.55']]
                           , columns=col
                        )
print(student_df)


stud_drop_level=student_df.drop(columns=['Marks'], level=1, inplace=True)
print(stud_drop_level)  # Display the DataFrame after dropping columns
print(student_df)