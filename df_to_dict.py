from typing import OrderedDict
import pandas as pd
from collections import OrderedDict

# create dataframe from csv
studentDf = pd.read_csv("csv/StudentData.csv")
print(studentDf)

# create dict from dataframe
studentDict = studentDf.to_dict()
print(studentDict)

print(studentDf.to_dict('list'))
print(studentDf.to_dict('series'))

print(studentDf.to_dict('split'))

print(studentDf.to_dict('index'))

print(studentDf.set_index('Name').to_dict()['Marks'])
print(studentDf.set_index('Name').T.to_dict('list'))

print(studentDf.to_dict(into=OrderedDict))
print(studentDf.to_dict(orient='records'))