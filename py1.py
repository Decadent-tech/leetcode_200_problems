import pandas as pd

# Create list
fruits_list = ['Apple', 10, 'Orange', 55.50]
print(fruits_list)

# Create DataFrame from list
fruits_df = pd.DataFrame(fruits_list,columns=['Fruits'],index=['Fruit1', 'Fruit2', 'Fruit3', 'Fruit4'])
print(fruits_df)

##########################################
price_list = ['50', '100', '60', '20']
print(price_list)

# Create DataFrame from list
price_df = pd.DataFrame(price_list)
print("Data type before : ", price_df.dtypes)

# Create DataFrame from list with type change
price_df = pd.DataFrame(price_list, dtype='float64')
print("Data type after : ", price_df.dtypes)
print(price_df)

# Create DataFrame from list with type change and column name
fruits_list = [['Apple', 'Banana', 'Orange', 'Mango'],[120, 40, 80, 500]]
print(fruits_list)

# Create DataFrame from list
fruits_df = pd.DataFrame(fruits_list)
print(fruits_df)

print("Data type before : ", pd.DataFrame(fruits_list))
print("transpose : ", pd.DataFrame(fruits_list).T)

#zips

fruits_list = ['Apple', 'Banana', 'Orange', 'Mango']
price_list = [120, 40, 80, 500]

print(pd.DataFrame(list(zip(fruits_list, price_list)),columns=['Fruits', 'Price']))

#######################dataframe from dict

import pandas as pd

# Create multiple lists
fruits_list = ['Apple', 'Banana', 'Orange', 'Mango']
price_list = [120, 40, 80, 500]

# Create dict
fruits_dict = {'Name': fruits_list,
               'Price': price_list}
print(fruits_dict)

# Create DataFrame from dict
fruits_df = pd.DataFrame(fruits_dict)
print(fruits_df)
