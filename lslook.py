# coding:utf-8
# python3 -- list列表操作（排序 查找 清空 反转 计数）
list_names = ["he", "li", "liu", "li", "fu", "chen", "liu", "li", "he", "chen",]
# 列表的查找index
print(list_names)
print(list_names[list_names.index("li")])
# count,元素计数
print(list_names.count("li"))
# reverse 反转列表
print(list_names)
list_names.reverse()
print(list_names)
# sort排序
list_names.sort()
print(list_names)
# extend 扩展（合并2个列表）
names = ["fa", "chu", "xi"]
list_names.extend(names)
print(list_names)
print(names)
# del names 删除变量，会报错
# del names

# clear 清空列表
# list_names.clear()
# print(list_names)
