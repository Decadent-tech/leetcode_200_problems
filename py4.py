import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat'], 
                'Age': [20, 21], 
                'Marks': [85, 77]
            }
student_df = pd.DataFrame(student_dict)

# Iterate all the rows of DataFrame
for index, row in student_df.iterrows():
    print(index, row)
#################################################################
import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}
student_df = pd.DataFrame(student_dict)
print(student_df)
print("##############################################################################")
# rename column
student_df = student_df.sort_values(by=['Marks'], ascending=False)
print(student_df)
print(student_df.to_dict())

print("##############################################################################")
import pandas as pd

# Create dict object
student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict, columns=["name", "marks"])
print(student_df)

student_df = pd.DataFrame(student_dict, index=["stud1", "stud2", "stud3"])
print(student_df)

print("###############################################################################")

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": ["85", "77", "91.54"]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("DataFrame with inferred data type : \n", student_df.dtypes)

# Change data types using astype
student_df = student_df.astype({"name": "string", "age": "int64", "marks": "float"})
print("DataFrame with changed data type : \n", student_df.dtypes)

print(student_df)
print("#################################################################################")
student_dict = {'name': 'Smith', 'age': 22, 'marks': 88.90}
student_df = pd.DataFrame(student_dict, index=['stud1'])
print(student_df)

print("#####################################################################################")

student_dict = {"Joe": 85.10, "Nat": 75.83, "Harry": 69.70}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict.items(), columns=["name", "marks"])
print(student_df)



student_dict = [{"name": "Joe", "age": 20, "marks": "85.58", "hobby": "smimming"},
                {"name": "Nat", "age": 21, "marks": "77.21", },
                {"name": "Harry", "age": 19, "marks": "91.54"}]
print(student_dict)

# Create DataFrame object
student_df = pd.DataFrame(student_dict)
print(student_df)
student_df = pd.DataFrame(student_dict, columns=["name", "marks"])


print("##########################################################################################")
student_dict = {"Grade A": {'Class A': {'name': 'Joe', 'marks': 91.56},
                            'Class B': {'name': 'Harry', 'marks': 87.90}},
                "Grade B": {'Class A': {'name': 'Sam', 'marks': 70},
                            'Class B': {'name': 'Alan', 'marks': 65.48}}}
print(student_dict)
# Create DataFrame from dict
student_df = pd.DataFrame.from_dict({(i, j): student_dict[i][j]
                                     for i in student_dict.keys()
                                     for j in student_dict[i].keys()},
                                    orient='index')
print(student_df)
