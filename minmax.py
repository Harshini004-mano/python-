# find the min without using max() / min()
# canditate: i will start by asuming the first element is both max and min
#then ,travel the list and update values if i find bigger/ smaller ones
nums =[5, 8, 2, 9, 1, 7]
max_num = min_num = nums[0]

for n in nums:
    if n > max_num: max_num = n
    if n < min_num: min_num = n

print("max: ", max_num)
print("min: ", min_num)