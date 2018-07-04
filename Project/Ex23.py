import sys

script, input_encoding, error = sys.argv

# 传入语言文件, 编码格式
def main(language_file, encoding, errors):

    # 依次读取行数
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    # 获取一行的最后一个
    next_lang = line.strip()
    # 获取下一行的原生字节数
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # 使用编码方式再次进行编辑,
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")
main(languages, input_encoding, error)
