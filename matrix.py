#Input : test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]] 
# Output : {5: [2, 0, 9], 8: [5, 4, 2], 10: [2, 3, 9]}
import pandas as pd
from typing import List, Dict
test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]]
res = dict(zip(test_list[0],test_list[1:]))
print(res) 
a=test_list[0]
b=test_list[1:]
d= {}
# Create a dictionary with keys from the first list and values from the rest
for i in range(0,len(a)):
    d[a[i]]=b[i]
print(d,a,b)
test_new_list = []
test_new = []

##doagonal elements 
test_col=[]
for i in range(len(test_list)):
  test_row=[]
  for j in range(len(test_list[i])):
    if i!=j:
      test_row.append(test_list[i][j])
  test_col.append(test_row)
print(test_col)
    