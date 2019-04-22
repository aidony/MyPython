#exl6.py 字符串和文本
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
test = types_of_people
print(f"{test}+x+y")
print(x)
print(y)
print(f"I said: {x}")#
print(f"I also said '{y}'")#

hilarious = "False"
joke_evalutution = "Isn't that joke so funny?!{}"
print(joke_evalutution.format(hilarious))

x = "This is the left side of "
y = "a string with a right side"
print(x + y)

#print("#字符串组合的几种形式")
#print("#1、f+双引号+方括号内+字符")
#print("#2、xxx.format()")
#print("#3、+")
#print("#4、用双引号直接放入")
