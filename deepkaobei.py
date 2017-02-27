# coding:utf-8
# python3 -- list列表操作（深拷贝copy）

import copy

# 深拷贝：拷贝的内容 不会随原列表list_names内容的更改而更改
list_names = ["he", "li", ["liu", "li"], "fu", "chen"]
list_names2 = copy.deepcopy(list_names)
list_names[3] = "平"
print(list_names)
print(list_names2)

# 多维列表
list_names[2][0] = "高"
print(list_names)
print(list_names2)
