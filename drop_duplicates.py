import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry", "Joe", "Nat"], 
                "age": [20, 21, 19, 20, 21],
                "marks": [85.10, 77.80, 91.54, 85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)

#student_df.drop_duplicates(inplace=True)  # Drop duplicate rows from DataFrame
#print(student_df)  # Display the DataFrame after dropping duplicates

# drop duplicate rows
#student_df = student_df.drop_duplicates(subset=['age','marks'])

#print(student_df)

#student_df = student_df.drop_duplicates(keep='last')

#print(student_df)
# drop all duplicate rows
#student_df = student_df.drop_duplicates(keep=False)

#print(student_df)

student_df = student_df.drop_duplicates(keep=False, ignore_index=True)

print(student_df)
#