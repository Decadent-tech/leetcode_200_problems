#a = set("geEks")

#s1 = {4, 12, 10, 9, 4, 13}
#sorted_s1 = sorted(s1)
#print(sorted_s1[0], sorted_s1[-1])  
#print(min(s1),max(s1))

#s1 = {5, 3 ,4 , 9 , 1 ,7}
#min_value = float('inf')
#max_value = float('-inf')
#for ele in s1:
#    if ele < min_value:
#        min_value = ele
#    if ele > max_value:
#        max_value = ele
#print("Minimum value:", min_value)
#print("Maximum value:", max_value)
#remove_value = 4
#if remove_value in s1:
#    s1.remove(remove_value)
#    print(f"Removed {remove_value} from the set.")
#print("Updated set:", s1)  
#print("popping", s1.pop())  # Pops an arbitrary element from the set
#print("Set after popping an element:", s1)  
a = [1,2,3,4]
b=[5,6,3,8]
common_elements = set(a) & set(b)
print("Common elements:", common_elements)

if any(item in b for item in a):
    print("There are common elements between the two lists: ")
else:
    print("There are no common elements between the two lists.")

a = [1, 2, 3, 4]
b = [2, 3, 5, 6]
c = [1, 2, 3, 7]

# Set comprehension to find common elements
res = {x for x in a if x in b and x in c}
print(f"Common elements: {res}")

missing_ele=[x for x in a if x not in b]
print(f"Missing elements from b: {missing_ele}")

s = "Python Programming"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
vowel_set = {char for char in s if char in vowels}
print(f"Vowels in the string: {vowel_set}")

s1='aacdfgh'
s2='abcfgh'
print(''.join(set(s1) ^ set(s2)))

S = "geeksforgeeks" 
S = S.lower()  # Convert to lowercase for case-insensitive comparison
S_set = set(S)
dict1={}
for ch in S:
    dict1[ch]= dict1.get(ch, 0) + 1
print("Character frequencies:")
for ch in S_set:
    if dict1[ch] == 1:

        print(f"{ch}: {dict1[ch]}")


def is_heterogram(s):
    s = s.lower()  # Case-insensitive
    seen = set()

    for ch in s:
        if ch.isalpha():  # Consider only letters
            if ch in seen:
                return False
            seen.add(ch)

    return True

# Example usage
input_str = input("Enter a string: ")
if is_heterogram(input_str):
    print("Yes, it's a Heterogram.")
else:
    print("No, it's not a Heterogram.")
