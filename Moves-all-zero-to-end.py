arr = [0, 1, 0, 3, 12 , 0 , 5 , 0 , 6 , 3]
result = [num for num in arr if num != 0]
zero_count = arr.count(0)
result += [0] * zero_count
print(result)