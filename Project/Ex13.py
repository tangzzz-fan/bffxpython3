# 使用参数初始化 py 文件
# 从模块中导入对应的函数模块, 这里是从 sys 模块中导入 argv 功能
from sys import argv

# read the WYSS section for how to run this
# 这里 用户 input() 的输入依次作为输入展示
# 脚本名 第一个参数 第二个参数 第三个参数
script, first, second, third = argv

print("The script is called:", script)
print("Your first variablfe is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


# 执行方法: 在控制台中切换对应的环境为 venv3.6, 然后使用命令:python3.6 Ex13.py 1st 2nd 3rd
# 这里 python3.6 之后的输入都是作为 argv 参数传递到运行环境中. 这里认为 输入的文件名 便是作为第一个参数使用. 传入的文件名如果错误, 则 脚本文件执行不了
# 要求几个参数 就需要几个参数,
# not enough values to unpack 如果参数个数不足, 提示参数不足.