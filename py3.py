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