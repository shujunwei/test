#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：test 
@File    ：循环.py
@Author  ：Administrator
@Date    ：2020/10/29 17:16 
'''

'''
循环语句
Python 中的循环语句有 for 和 while。

'''

'''
while 循环
while 语句的一般形式：

while 判断条件(condition)：
    执行语句(statements)
'''

# 同样需要注意冒号和缩进
# 无限循环,我们可以通过设置条件表达式永远不为 false 来实现无限循环


# 表达式永远为 true
# x = 1
# while x == 1:
#     print('无限循环')
# 你可以使用 CTRL+C 来退出当前的无限循环。
# 无限循环在服务器上客户端的实时请求非常有用。



# 表达式永远为 true，无限循环
# var = 1
# while var == 1:
#     num = input("请输入你的数字：")
#     print("你输入的数字是：",num)



# 使用了 while 来计算 1 到 100 的总和：


# y = 1
# sum =  0
#
# while y <= 100:
#     sum = sum + y
#     y +=1
#     print(sum)
# print("1 到 100 的和为 %d" % sum)



# while 循环使用 else 语句
# 在 while … else 在条件语句为 false 时执行 else 的语句块。

# x = 0
# while x < 5:
#     x = x+1
#     print(x)
# else:
#     print(x,"大于或等于 5")




'''
for 语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
for循环的一般格式如下：
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''

# list = [1,2,3,4,5,6,7,8,9]
# str = 'Hello Word'
#
# for i in list:
#     print(i)
#
# for i in str:
#     print(i)


'''
# break语句用于跳出当前循环体：
# 执行脚本后，在循环到 "Runoob"时会跳出循环体：
'''

# list = [1,2,3,4,5,6,7,8,9]
#
# for i in list:
#
#     if i == 6:
#         print('如果i等于6，跳出循环。')
#         break
#     print('循环数据：',i)
#
# else:
#     print("没有循环数据")
#
# print('循环结束')

'''
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
'''

# list = [1,2,3,4,5,6,7,8,9]
#
# for i in list:
#
#     if i == 6:
#         print('如果i等于6，跳出循环。')
#         continue
#     print('循环数据：',i)
#
# else:
#     print("没有循环数据")
#
# print('循环结束')



# while 中使用 continue：

# n = 0
#
# while n <= 5:
#     n +=1
#     if n == 3:
#         print("n==:",n)
#         continue
#
#     print(n)




'''
range()函数
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，
'''

# for i in range(100):
#     print(i)

# 也可以使用range指定区间的值：

# for i in range(1,20):
#     print(i)


# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):

# for i in range(1,20,2):
#     print(i)

# 负数

# for i in range(-1,-20,-2):
#     print(i)

# 可以结合range()和len()函数以遍历一个序列的索引,如下所示:

# list = ['Jack','Tom','Rose']
# for i in range(len(list)):
#     print(i,list[i])



# 使用range()函数来创建一个列表：

# lis1 = list(range(20))
# print(lis1)


'''
break 和 continue 语句及循环中的 else 子句
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
'''

# while 中使用 break：

# i  = 0
# while i <= 5:
#     i +=1
#     if i == 3:
#         print("i == 3, break循环终止，")
#         break
#     print(i)
#
# print("循环结束")


# i = 0
#
# while i <= 5:
#     i +=1
#     if i == 3:
#         print("continue跳过3，继续循环")
#         continue
#     print(i)
# print("循环结束")


'''
循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。
如下实例用于查询质数的循环例子:
'''
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, ' 是质数')



'''
pass 语句
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句，如下实例

'''

# while True:
    # pass



# s = 100
# for i in range(100):
#     s +=i
# print("1 到 100 的和为 %d" % s)




