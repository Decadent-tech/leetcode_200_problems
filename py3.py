#Only one pair adds up to the target (2 + 7 = 9), so the program prints their indices.
numbers = [2,7,11,15]
target = 9
hashMap = {}
for index, num in enumerate(numbers):
    diff = target - num #7 , 2 ,-2
    if diff in hashMap:
        print([hashMap[diff], index]) #

    hashMap[num] = index #2 - 0,7 - 1,11 - 2,15 - 3

#Kadane's Algorithm to find the maximum sum of a contiguous subarray in a list of integers.
def maxSubArray(nums):
    ans = nums[0]#-2,1
    currentSum = 0

    for i in nums:
        currentSum += i#1,-2,-3,1,-1,2,1,-5,4

        if ans < currentSum:
            ans = currentSum #1,-2,-3,1 ,0,2,3

        if currentSum < 0:
            currentSum = 0#0,0,0,0

    return ans

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

####################################################################################
x = 24 
# Check the remainder dividing x by 2 is 0
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Checking another number    
x = 7

if x % 2 == 0:

  print("Even")
else:
    print("Odd")
#########################################
a=[1, 2, 3, 4, 5]
res = map(lambda num:str(num)+"Even" if num%2 ==0 
          else str(num)+"Odd", a)
print(list(res))  # ['1Odd', '2Even', '3Odd', '4Even', '5Odd']

#############################################
# Inputing Natural Number
number = int(input("Enter the Natural Number: "))

# j ranges from 1 to n
for j in range(1, number+1):

    # Initializing List
    a = []

    # i loop ranges from 1 to j
    for i in range(1, j+1):
        print(i, sep=" ", end=" ")
        if(i < j):
            print("+", sep=" ", end=" ")
        a.append(i)
    print("=", sum(a))

print()

#####################################################
n= int(input("Enter a number to check if it is prime: "))
import math
is_prime = True
for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
print(is_prime)

###########################################

# Function to print full pyramid pattern
def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()
   
full_pyramid(5)

##############################################
