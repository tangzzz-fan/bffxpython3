# Functions Can Return Something
# 这里只有在 {} 中才可以执行计算操作, 否则只是按照运算后的数据使用, 比如作为运算后的字符串或者数字
# 使用两个参数, python 中的参数也可以返回两个数据,
# 典型例子: Python 中的数字交换位置.
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


def substract(a, b):
    print(f"Substract {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"Mutiply {a} * {b}")
    return a * b


def devide(a, b):
    print(f"Deviding {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# 字符串格式化输出 使用变量字符串接收要进行运算的数据.
what = add(age, substract(height, multiply(weight, devide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
print(f"That becomes: {what} Can you do it by hand?")
