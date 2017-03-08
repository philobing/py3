# coding:utf-8
name = "my nam\te is {name} and {age} "
# 首字母大写
print(name.capitalize())
# 计算字符
print(name.count("m"))
print(name.center(50, "-"))
# 以什么结尾
print(name.endswith("ng"))

print(name.expandtabs(tabsize=30))
# 查找
print(name.find("a"))
# 字符串切片
print(name[name.find("e"):])
# 格式化输出
print(name.format(name='li ming', age=20))
# 字典形式的格式化输出
print(name.format_map({'name': 'li ming', 'age': 18}))
# 阿拉伯的数字
print('bus8'.isalnum())
# 纯英文字符
print('buS'.isalpha())
# 十进制数
print('66666'.isdecimal())
# 整数
print('66666'.isdigit())
# 判断 字符串 是不是一个合法的 标识符（是否是一个合法的变量名）
# 中文也可以做变量名，但是不推荐使用中文
print('a66666'.isidentifier())
# 小写
print('a66666'.islower())
# 大写
print('CEO66'.isupper())
# 数字
print('666'.isnumeric())
# 空格
print(' '.isspace())
# 是不是标题
print('My Name Is'.istitle())
# 是否打印（在tty file, drive file文件），用途少
print('My Name Is'.isprintable())
# join的用法
print('My Name Is'.join("===="))
# 推荐用法
print(''.join(['li', 'chen', 'dong']))
print('+'.join(['1', '2', '3']))

print(name.ljust(50, '*'))
print(name.rjust(50, '*'))

print("CEO".lower())
print("ceo".upper())
# 左边去空格
print("\nceo".lstrip())
print("ceo\n".rstrip())
print("\nceo\n".strip())
print('********')
