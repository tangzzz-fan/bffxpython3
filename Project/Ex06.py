types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# 格式化字符串
y = f"Those who know {binary} and those who {do_not}."

# z1 = "Just test format '{}'".format(binary)
# {} 如果花括号作为运算符, 则不应该在其中先填上东西, 要使用 {} 格式化, f/format 不可少
z2 = "Another test '{}'"
z3 = z2.format(binary)

print(x)
print(y)
print(z3)

print(f"I said: {x}")
# 单引号, 双引号的区别
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# 格式化字符串的一般形式
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."

e = "a string with a right side."

print(w+e)
