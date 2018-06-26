# 初始化一个格式化器, 使用这个 formatter 的需要提供四个参数, 参数的类型没有限制, 参数之间的类型没有限制, 依然可以做运算操作
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# 此处, formatter 可以作为字符串使用.
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
my_name = "Tango"
print(formatter.format(1, "Hello", 23 + 34, f'World {my_name}'))
