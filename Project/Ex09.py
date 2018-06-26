# 关于格式化字符串的总结
# 1 变量, 在 print() 中直接被调用
# 2 formatter 格式化
# 3 f'Hollo {}' 花括号计算
# Here's some new strange stuff, remember type it exactly. 2
days = "Mon Tue Wed Thu Fri Sat Sun"
# \n 换行
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# 变量计算
print("Here are the days: ", days)
print("Here are the months: ", months)

# 多行字符串 控制换行 """ ... """
print("""
 There's something going on here.
 With the three double-quotes.
 We'll be able to type as much as we like.
 Even4linesifwewant,or5,or6.
 """)
