#without counter
nums = [1, 2, 2, 3, 3, 4]
freq = {}
for i in nums:
    freq[i] = freq.get(1,0)+1
print(freq)