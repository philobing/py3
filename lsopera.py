# coding:utf-8
# list列表操作
list_names = ["he", "li", "fu", "chen"]
# 切片操作
print("--切片操作--")
print(list_names[0])
print(list_names[1:3])
print(list_names[3])
print(list_names[-2])

# 增加操作
print("--增加操作--")
list_names.append("dao")
print(list_names)

# 插入操作
print("--插入操作--")
list_names.insert(1, "ma")
print(list_names)
list_names.insert(3, "liu")
print(list_names)

# 更改操作
print("--更改操作--")
list_names[3] = "fen"
print(list_names)

# 删除元素
print("--删除操作--")
# remove 找里面元素进行删除
list_names.remove("dao")
print(list_names)

# delete
del list_names[2]
print(list_names)

# pop 删除末尾元素
list_names.pop()
print(list_names)
# del list_names[2] = list_names.pop(2)
list_names.pop(1)
print(list_names)
