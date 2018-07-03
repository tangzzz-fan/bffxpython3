# Functions and Files
from sys import argv

script, input_file = argv


def print_all(f):
    # 读取文件
    print(f.read())


def rewind(f):
    # 文件重定向
    f.seek(0)


def print_a_line(line_count, f):
    # 按行输出 readline 遇到 \n 自动停止
    # read() 读取全部的文件.
    print(line_count, f.readline())


# 根据文件名 打开文件
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
