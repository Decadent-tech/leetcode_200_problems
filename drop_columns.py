import pandas as pd
import numpy as np

student_dict = {"name": ["Joe", "Sam", "Harry"], "age": [20, 21, 19], "marks": [85.10, np.nan, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)

student_df = student_df.dropna(axis='columns')
print(student_df)

student_dict = {"name": ["Joe", "Sam", np.nan, "Harry"], "age": [np.nan, np.nan, np.nan, np.nan],
                "marks": [85.10, np.nan, np.nan, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)

# keep column with 3 or more non-NA values
student_df = student_df.dropna(axis='columns', thresh=3)

print(student_df)


student_dict = {"name": ["Joe", "Sam", "Harry"], "age": [np.nan, np.nan, np.nan], "marks": [85.10, np.nan, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)

# drop marks column with NaN
student_df = student_df.dropna(axis='columns', subset=[0, 2])

print(student_df)


student_dict = {"name": ["Joe", "Sam", "Harry"], "age": [20, 21, 19], "marks": [85.10, np.nan, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)

# drop marks row with NaN
student_df.dropna(inplace=True)

print(student_df)