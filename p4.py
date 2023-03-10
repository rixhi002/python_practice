nums = [5, 9, 13, 23, 35, 40, 43, 47, 50]
key=9
low = 0  
high = len(nums) - 1  
mid = 0  
while low <= high:  
    mid = (high + low) // 2  
    if nums[mid] < key:  
        low = mid + 1  
    elif nums[mid] > key:  
        high = mid - 1  
    else:  
        result= mid  
if result == key:  
    print("Element is present at index", result)  
else:  
    print("Element is not present in list1")  
