# reading fils
from sys import argv

# script 脚本名, 即输入的第一个参数作为脚本名, 第二个参数作为文件名
script, filename = argv

# 打开文件 类似文件句柄的方式命名打开的文件叫 txt, 后续对文件的操作就可以直接对 txt 操作.
# 此时的 txt 不可以进行读写操作.
# 添加 w,r 等权限修饰 一般是为了保证文件安全操作.
txt = open(filename)


print(f"Here is your file {filename}")
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("请输入: > ")

# 打开文件
txt_again = open(file_again)

# 读取文件的函数
print(txt_again.read())
# 关闭文件
txt_again.close()