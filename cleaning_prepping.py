import pandas as pd 
import numpy as np
df = pd.DataFrame(data={'col1':[np.nan, np.nan, 2,3,4, np.nan, np.nan]})
print(df)

#FILLED FORWARD by 1

df.fillna(method='pad', limit = 1 , inplace=True)
print(df)

df.fillna(method='bfill',inplace=True)
print(df)

df.dropna(inplace=True)
print(df)

# Drop columns that have any nans
#df.dropna(axis=1)
# Only drop columns which have at least 90% non-NaNs
#df.dropna(thresh=int(df.shape[0] * .9), axis=1)

#np.where example 
df = pd.DataFrame(data={'col1':[np.nan, np.nan, 2,3,4, np.nan, np.nan]})
print(df)   
df['col1'] = np.where(df['col1'].isnull(), 'foo','bar')
print(df)
df['new_column'] = np.where(df['col1'].str.startswith('foo'), True, False)
print(df)


#te4st np.all

df_all = pd.DataFrame(data={'col1':np.random.randint(0, 10, 10), 'col2':np.random.randint(-10, 10, 10)})
print(df_all)

print(np.all(df_all > 0, axis=1))  # Check if all values in each row are greater than 0
print(np.all(df_all['col2'] > 0, axis=0))  # Check if all values in each column are greater than 0
print((df_all != str).any) # Check if all values in the DataFrame are greater than
assert(df['col1'] != str).any()

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
foo = 'is this string'
bar = 'like that string?'
print(fuzz.ratio(foo, bar))


from dateutil.parser import parse
dt = parse("Today is January 1, 2047 at 8:21:00AM", fuzzy=True)
print(dt)

#deduping 
# List of duplicate character names
contains_dupes = [
'Harry Potter', 
'H. Potter', 
'Harry James Potter', 
'James Potter', 
'Ronald Bilius \'Ron\' Weasley', 
'Ron Weasley', 
'Ronald Weasley']
# Print the duplicate values
print(process.dedupe(contains_dupes))
# Print the duplicate values with a higher threshold
print(process.dedupe(contains_dupes, threshold=90))

#somthing in parse 

dt = parse("May 18, 2049 something something", fuzzy=True)
print(dt)

#from scikit-learn

# At start of project
from sklearn import preprocessing
# And let's create a random array of ints to process
ary_int = np.random.randint(-100, 100, 10)
print(ary_int)
# And some str to work with
ary_str = ['foo', 'bar', 'baz', 'x', 'y', 'z']

from sklearn.preprocessing import LabelEncoder
l_encoder = preprocessing.LabelEncoder()
l_encoder.fit(ary_str)
LabelEncoder()
# Transform
print(l_encoder.transform(['foo']))
print(l_encoder.transform(['baz']))
print(l_encoder.transform(['bar']))

print(list(l_encoder.classes_))

# Create dictionary of mappings
#abel_dict = dict(zip((l_encoder.classes_),(l_encoder.transform(l_encoder.classes_))))
# Print the label dictionary
label_dict = {k: v for k, v in zip(l_encoder.classes_, l_encoder.transform(l_encoder.classes_))}
print(label_dict)

from sklearn.preprocessing import OrdinalEncoder
o_encoder = OrdinalEncoder()
ary_2d = [['foo', 'bar', 'baz'], ['x', 'y', 'z']]
o_encoder.fit(ary_2d) # Fit the values
print(o_encoder.transform(ary_2d)) # Transform the values


from sklearn.preprocessing import OneHotEncoder
hot_encoder = OneHotEncoder(handle_unknown='ignore')
hot_encoder.fit(ary_2d)
print(hot_encoder.categories_)

print(hot_encoder.transform([['foo', 'foo', 'baz'], ['y', 'y', 'x']]).toarray())  # Transform the values

#dummie data
new = pd.get_dummies(df)
print(new)

from sklearn.preprocessing import MinMaxScaler
mm_scaler = MinMaxScaler(feature_range=(0, 1)) 
print(mm_scaler.fit([ary_int]))
print(mm_scaler.data_max_)