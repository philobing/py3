# coding:utf-8

# 多写，写的少

# 嵌套列表

product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 9800),
    ('Bike', 800),
    ('Watch', 10600),
    ('Coffee', 30),
    ('Python', 120),
]
salary = input("Input your salary:")
shopping_cart = []
if salary.isdigit():
    salary = int(salary)
    while True:
        '''
        for item in product_list:
            print(product_list.index(item), item)
        '''
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("选择要买什么？>>>：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:  # 说明买的起
                    shopping_cart.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart, your current balance is \033[31;1m%s\033[0m" % (p_item, salary))
                else:
                    print("\033[41;1m 你的余额只剩 [%s] 了,买不起啦\033[0m" % salary)
            else:
                print("product code [%s] is not exist!" % user_choice)
        elif user_choice == 'q':
            print("-----shopping list-----")
            for p in shopping_cart:
                print(p)
            print("Your current balance:", salary)
            exit()
        else:
            print("invalid option")
else:
    print("薪资输入有误")
