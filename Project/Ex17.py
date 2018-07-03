# more files
# copy file to another file

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

# 检查是否存在对应的文件
print(f"Does the output file exist? {exists(to_file)}")

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# 打开文件
out_file = open(to_file, 'w')
# 将数据写入到文件中
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()

