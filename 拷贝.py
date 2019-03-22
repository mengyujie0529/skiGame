'''实现拷贝的几种方式（很重要）'''
old_list=[1,2,3,4,5]

#1.通过直接赋值的方式，进行列表的拷贝
# 两个列表地址（id）是一样的，操作也是同步的
new_list=old_list
print(id(old_list))
print(id(new_list))

old_list.append(6)
print(old_list)
print(new_list)

#2.浅拷贝,使用copy()
#两个列表除了刚开始的数据是一样的，之后没有任何关系
#两个列表操作不同步，地址（id）也是不同的
new_list2=old_list.copy()
print("******************浅拷贝************************")
print(id(old_list))
print(id(new_list2))

new_list2.append("浅拷贝")
old_list.append("999")
print(old_list)
print(new_list2)

#3.深拷贝
#
#
import copy
new_list3=copy.deepcopy(old_list)
print("****************深拷贝*********************")

print(id(new_list3))
print(id(old_list))
