# colors = ["red","green","blue","yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)


for k in range(5):#start
    print(k+1)

for k in range(1,2000):
    print(k+1)
for k in range(1,14,2):
    print(k)



for i in range(3):#start
    print(i)

i = 0
while(i<3):
    print(i)
    i = i+1


i =int(input('enter the number: '))#start
while(i<=38):
    i = int(input('enter the number: '))
    print(i)
print("done with the loop")


count = 5#start
while(count>0):
    print(count)
    count = count-1
else:
    print("i am inside else")