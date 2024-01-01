# mn=int(input())
# x=input()
# x2=input()
# y=" ".join([x])
# y2=" ".join([x2])
# array=y.split(" ")
# array2=y2.split(" ")
# if len(array) and len(array) == mn:
#     for i in range(0, len(array)):
#         array2[i] = int(array2[i])
#         # print(array2, end=" ")
#         array[i] = int(array[i])
#         # print(array, end=" ")
        
#     sum=0
#     for i in range(len(array)):
#         # print(x1[i] , y1[i])
#         power=(array[i]-array2[i])**2
#         sum+=power
        
#     print(round(sum**0.5, 2))
# else:
#     print("its wrong")
    
#############################################
a1=[]    
b1=[]
bod=int(input())
for i in range(bod):
    a=int(input())
    a1.append(a)
    
for i in range(bod):
    b=int(input())
    b1.append(b)
print(a1, b1)

for i in range(0, len(a1)):
    b1[i] = int(b1[i])
    # print(array2, end=" ")
    a1[i] = int(a1[i])
    # print(array, end=" ")
    
sum=0
for i in range(len(a1)):
    # print(x1[i] , y1[i])
    power=(a1[i]-b1[i])**2
    sum+=power
    
print(round(sum**0.5, 2))