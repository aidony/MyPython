my_name = 'Bruce' # my name，
my_ege = 26 # my ege
my_weight = 66 # kg
my_No_1 = 13.0
my_No_2 = 4.0
my_No_3 = my_No_1 / my_No_2 # = 13.0 / 4.0 = 3.25
my_No_4 = my_No_1 % round(my_No_3) # = 13 % round(3.25) = 13 % 3 =1.0
print(f"我的名字是：{my_name}。注意！！！变量要以字母开头，不能以数字开头！！！")
print(f"我的年龄是：{my_ege}。")
print(f"我的年龄是：{my_weight}公斤。")
total = my_ege + my_weight
print(f"Test 'total' = {total}.")
print(f"{my_No_4}")#注意，运算放到前面变量定义中去
