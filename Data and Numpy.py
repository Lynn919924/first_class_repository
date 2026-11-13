import numpy as np
scores = np.array([45, 82, 60, 59, 91, 73])
# 让每一个分数都去和 60 比一比
# 此时，mask 变成了：[False, True, True, False, True, True]
# 为什么？因为 45>=60是False，82>=60是True... 依此类推。
passed = sorted(scores[scores >= 60])
print(passed)


arr1 = np.array(42)
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
my_list = [arr1, arr2, arr3]
print(arr1)
print(arr2)
print(arr3)
print(arr3.ndim)
print(arr1.shape)
print(arr2.size)
print(arr3*2)
print(arr2[1:3])
print(my_list*2)

d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(d.ndim)
print(d)
print(d.shape)#2(两堆东西)2（每一堆东西有2行3列）3

my_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(my_arr[0:2, 2])#是[3 8]不是[[3] [8]]（arr[0:2, 2] -> 列用数字，结果变 1 维：[3 8]
                      # arr[0:2, 2:3] -> 列用切片，结果保持 2 维：[[3] [8]]）

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print(a[1:, 1:3])
print(a[:, ::-1])
print(a[:, -1:])
print(a[0, ::-1])
print(a.transpose())

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)#<U6（https://chat.deepseek.com/share/f2lqvhmfdk4s1w75g5)

new_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(new_arr.reshape(2, 4).base)#用.base去查找该内存的原数据（若为none,则是自己新开的）

