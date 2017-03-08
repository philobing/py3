# coding:utf-8
# 字典的操作 key - value
info = {
    'sheep01': "liu",
    'sheep02': "ma",
    'sheep03': "fei"
}
sheep = {
    'color_sheep01': "red",
    'color_sheep02': "black",
    'color_sheep03': "yellow",
}
print(info)
# 不推荐使用这种方式查找
print(info["sheep01"])
# 安全查找
print(info.get('sheep03'))
# 修改
info["sheep01"] = "刘"
# 增加
info["sheep04"] = "chen"
print(info)

# del 是python中内置的通用方法
del info["sheep02"]
print(info)
# pop
info.pop("sheep01")
print(info)
# popitem() 随机删除
info.popitem()
print(info)
# 将一个字典更新到另一个字典中
info.update(sheep)
print(info)
# 把字典转成列表item
print(info.items())
# 字典fromkeys初始化
c = dict.fromkeys([6, 7, 8], "test")
print(c)
print("-------")
# 字典的循环
for i in info:
    print(i)
print('--------')
for i in info:
    print(i, info[i])
print("---------")
# 在数据量小的时候使用，推荐不使用
for k, v in info.items():
    print(k, v)
