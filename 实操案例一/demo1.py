# coding=utf-8
"""
任务1：向文件输出'奋斗成就更好的你'
"""
# 方案一：使用print打印

# f = open('test.txt', 'w')
# print('奋斗成就更好的你', file == f)
# f.close()


# 使用文件读写操作
with open('test1.txt', 'w') as file:
    file.write('奋斗成就更好的你')
