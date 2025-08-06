arr = [4,5,3,2,8,1,6]
def find_max(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value
def find_min(arr):
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value
def find_missing(arr):
    for i in range(find_min(arr), find_max(arr) + 1):
        if i not in arr:
            return i
        
print("Missing number in the array:", find_missing(arr))