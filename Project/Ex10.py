
# 转义字符的使用
# table 空格输出
tabby_cat = "\tI'm tabbed in."
# 换行
persian_cat = "I'm split\non a line."
# 输出 \
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
 """

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
