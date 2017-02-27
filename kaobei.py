# coding:utf-8
# python3 -- list列表操作（拷贝copy）

# 注意文件命名方式：不能 与关键字copy等发生冲突

# 浅拷贝，只拷贝第一层，2层以上 都是拷贝元素的地址
list_names = ["he", "li", ["liu", "li"], "fu", "chen"]
list_names2 = list_names.copy()
list_names[3] = "平"
print(list_names)
print(list_names2)

# 只是name，指向了list_names这个列表存储地址
name = list_names
print(name)
# 多维列表：，所以2层以后的元素，会跟着原来的列表改变
list_names[2][0] = "高"
print(list_names)
print(list_names2)
