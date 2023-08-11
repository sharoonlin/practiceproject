#if 判斷句

#1.
#如果 我肚子餓
#     我就去吃飯

hungry=True
if hungry:
    print("我就去吃飯")

#if 我肚子餓:
 #   我就去吃飯

#2.
#如果 今天下雨
#     我就開車去上班
#否則
#      我就走路去上班

rainy=False #定義background 
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")

#3. 
#如果  你考100分
#      我給你1000元
#或是如果 你考80分以上
#      我給你500元
#或是如果  你考60分以上
#        我給你100元
#否則
#        你給我300元


score=90
if score==100:
    print("我給你1000元")
elif score >= 80:
    print("我給你500元")
elif score >=60:
    print("我給你100元")
else:
    print("你給我300元")

score=90
rainy=True
if score==100 and rainy:
    print("我給你1000元")
else:
    print("你給我100元")

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1 #判斷num1最大的
    elif num2>=num1 and num2>=num3:
        return num2 #判斷num2最大的
    else:
        return num3 #判斷num3最大的
    print(max_num(2,3,5))
