#列表list 列表用法
scores=[90,70,60,50,80]
friends=["小黑","小黃","小綠"]
things= [90,"小黑",True]
pharse="Hello Mr.White"
print(scores[0:4]) #print score第0個位置 #到第三位
print(things[0])
print(things[:2])#從最前面開始
print(pharse[0:]) #包含在最後面
print(pharse[6:])

scores.extend(friends)
print(scores) #scores 前面再加上friend 的字串

scores.append(30) #append 列表後再加一"值"
print(scores)

scores.insert(2,30)
print(scores)

scores.remove(90) #把90這個值刪除
print(scores) 

score1= 90
score2= 70
score3= 60
score4= 50
score5= 80


