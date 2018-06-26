
# 交互式输出使用, end 出现在字符串中表示结束
# 使用 input() 接收用户输入 ~~ cin

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
