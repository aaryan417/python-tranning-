import numpy as np
marks =np.array([80,76,90,99,65,44])

print("total", np.sum(marks))
print("avrage", np.mean(marks))
print("highst", np.max(marks))
print("lovest", np.min(marks))
print(len(marks))

# add 10 in each element of arr
arr = np.array([1, 2, 3, 4, 5])
print(arr+10)


# Multiply every element by 5

arr5 = np.array([2, 4, 6, 8])
print(arr5*5)



# Square Numbers

arr6 = np.array([1, 2, 3, 4, 5])
print(arr6*arr6)



# Zeros Array
arr10 = np.zeros(10, dtype=int)
print(arr10)