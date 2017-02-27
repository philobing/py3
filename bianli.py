# coding:utf-8
# python3 -- list列表操作 （遍历）
list_names = ["he", ["liu", "li"], "li",  "fu", "chen", "liu", "gao"]
# 步长切片
# range(1, 10, 2)
print(list_names[0:-1:2])
print(list_names[::2])
# 表示0 到 -1 ，从头到尾打印
print(list_names[:])

for i in list_names:
    print(i)
