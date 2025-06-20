import sys


d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

myKeys = list(d.keys())
print(myKeys.sort())

# Sorted Dictionary
sd = {i: d[i] for i in myKeys}
print(sd)

########################################################
# Initializing key-value pairs
d = {2: 56, 1: 2, 5: 12, 4: 24}

print("Dictionary", d)

# Sorting and printing dictionary keys aand values
d1 = sorted(d.items(), key=lambda x: x[0])
print("Sorted Dictionary by keys:", d1)
# Sorting and printing dictionary keys and values
d2 = sorted(d.items(), key=lambda x: x[1])   
print("Sorted Dictionary by values:", d2)

####sum of dictionary values
sum = 0
for i , j in d.items():
    sum += j
print("Sum of values in dictionary:", sum)

print(sys.getsizeof(d))

from operator import itemgetter

# Initializing list of dictionaries
data_list = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19}]

# using sorted and itemgetter to print list sorted by age
print("The list printed sorting by age: ")
print(sorted(data_list, key=itemgetter('age')))
############################################################################

d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1.copy()
for key, value in d2.items():
    d3[key] = value

print(d3)