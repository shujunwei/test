#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：test 
@File    ：条件控制.py
@Author  ：Administrator
@Date    ：2020/10/29 16:13 
'''

'''

条件控制
Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。
4个空格或者tab缩进
'''

'''
if 语句
Python中if语句的一般形式如下所示：

'''

# a = 1
# if a < 2:
#     print("a < 2")
# elif a > 2:
#     print("a > 2")
# else:
#     print('其他')

# if语句的关键字为：if – elif – else
'''
注意：
1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
。
'''

# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
#
# ### 退出提示
# input("点击 enter 键退出")




'''
if中常用的操作运算符:

操作符	描述
<	    小于
<=	    小于或等于
>	    大于
>=	    大于或等于
==	    等于，比较两个值是否相等
!=	    不等于    
'''


'''
if 嵌套
在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
'''


# num=int(input("输入一个数字："))
# if num%2==0:
#     if num%3==0:
#         print ("你输入的数字可以整除 2 和 3")
#     else:
#         print ("你输入的数字可以整除 2，但不能整除 3")
# else:
#     if num%3==0:
#         print ("你输入的数字可以整除 3，但不能整除 2")
#     else:
#         print  ("你输入的数字不能整除 2 和 3")

















