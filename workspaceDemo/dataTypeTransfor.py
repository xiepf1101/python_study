#coding=utf-8
#数据类型转换

#转换为int
int_ = int("110")
print(int_)

#转换为float
float_ = float("11.12")
print(float_)

#转换为字符串
str_ = str(["110",120])
print(str_)

#转换为表达式字符串
repr_ = repr("xxx")
print(repr_)

#
eval_ = eval("str")
print(eval_)

#将字符串转换为元组 tuple
tuple_ = tuple("123")
print(tuple_)

#将字符串转换为列表list
list_ = list("123")
print(list_)

#将字符串转换为集合
set_ = set("123")
print(set_)

#dict

#将字符串转换为冻结集 frozenset
frozenset_ = frozenset("123")
print(frozenset_)

#将数字转换为字符（没看懂）
chr_ = chr(2)
print(chr_)

#将单个字符转换为整数值
ord_ = ord("a")
print(ord_)

#将整数转换为16进制字符串
hex_ = hex(123)
print(hex_)

#将整数转换为8进制字符串
oct_ = oct(123)
print(oct_)