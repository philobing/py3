# coding:utf-8
# 三级菜单 字典 列表
# Author：coco

data = {
    '北京': {
        "昌平": {
            "沙河": {"oldboy", "test"},
            "天通苑": {"链家地产", "我爱我家"},
        },
        "朝阳": {
            "望京": {"奔驰", "陌陌"},
            "国贸": {"CICC", "HP"},
            "东直门": {"Advent", "飞信"},
        },
        "海淀": {},
    },
    '山东': {
        "德州": {},
        "青岛": {},
        "济南": {},
    },
    '广东': {
        "东莞": {},
        "常熟": {},
        "佛山": {},
    },
}
while True:
    for i in data:
        print(i)
    choice = input("选择进入>>:")
    if choice in data:
        while True:
            print("hello")
