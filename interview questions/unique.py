nums = [1, 2, 2, 3, 1, 4, 3]
unique =[]
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)