formatter = "{} {} {} {}"
#one = 1
#two = 2
#three = 3
#four = 4

print(formatter.format(1, 2, 3, 4))
#print(formatter.format(1,2,3,4))#
#print(formatter.format(one, two, three, four))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))#fasle & true 与True & False有区别
print(formatter.format(formatter, formatter, formatter, formatter))
#print(formatter.format("formatter1”, “formatter1”, “formatter3”, “formatter4"))#注意引号的中英文切换！！！
print(formatter.format("formatter1", "formatter1", "formatter3", "formatter4"))
print(formatter.format(
"Try yourself",
'Hi',
"Maybe you're right!",
'Stop'
))
