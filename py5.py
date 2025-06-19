def summation(test_up):
    if len(test_up) == 0:
        return ValueError("List is empty")
    if not all(isinstance(x, (int, float)) for x in test_up):
        return TypeError("List must contain only numbers")
    iterable = (x for x in test_up)
    return sum(iterable)
test_up = [1, 2, 3, 4, 5]
result = summation(test_up)
print("Sum of the list:", result)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)

combined = zip(tuple1, tuple2, tuple3)
result = tuple(map(sum, combined))
print(result)

test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]

# printing original list
print("The original list is : " + str(test_list))

# initializing Custom eles
cus_eles = [6, 7, 8]

# Row-wise element Addition in Tuple Matrix
# Using zip() + list comprehension
res = [[(idx+ (val,)) for idx in key] for key, val in zip(test_list, cus_eles)]

# printing result 
print("The matrix after row elements addition : " + str(res))
print("----------------------------------------------------------------------------------")

a = [1, 2, 3, 4, 5]

# Creating list of tuples using list comprehension
res = [(n, n**3) for n in a]
print(res)
print(list(map(lambda n:(n,n**3), a)))