# 文件操作 文件读写

# close save and exit
# read
# readline: 依次读取文件中的每一行
# truncate: empties the file
# write('stuff'): 将stuff 写入到文件中
# seek(0) move the location to the beginning of file

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# 打开文件. 指定使用的读写权限
target = open(filename, "w")

print("Truncating the file, good bye")
# 清空文件
target.truncate()

print("I am going to ask you for 3 lines")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I am going to write these to the file")
target.write(line1)
target.write(line2)
target.write(line3)

print("And finally, we close it")
target.close()
