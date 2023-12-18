# p=int(input())
# x1=[]
# y1=[]
# for i in range (p):
#     x=int(input())
#     y=int(input())
#     x1.append(x)
#     y1.append(y)
    
# # print(x1 ,y1)
# sum=0
# for i in range(len(x1)):
#     # print(x1[i] , y1[i])
#     power=(x1[i]-y1[i])**2
#     sum+=power
    
# print(round(sum**0.5, 2))

###############################################

# mn=int(input())
# x=input()
# x2=input()
# y=" ".join([x])
# y2=" ".join([x2])
# array=y.split(" ")
# array2=y2.split(" ")
# sum=0
# for i in range(0, len(array)):
#     array2[i] = int(array2[i])
#     # print(array2, end=" ")
#     array[i] = int(array[i])
#     # print(array, end=" ")
    
# sum=0
# for i in range(len(array)):
#     # print(x1[i] , y1[i])
#     power=(array[i]-array2[i])**2
#     sum+=power
    
# print(round(sum**0.5, 2))

#############################################
# list=[]
# p=int(input())
# for i in range (p):
#     x=input()
#     # print(i)
#     list.append(x)
#     y=" ".join([x])
#     # x=[input1,input2,input3,input4]
#     list=y.split(" ")
#     for j in range(0, len(list)):
#         list[j] = int(list[j])
#         print(list, end=" ")

###########################################

# c=int(input())
# a = [ int(c) for c in input().split(" ")]
# print(a)



x=input()
a = [ int(c) for c in input().split(" ")]
b = [ int(c) for c in input().split(" ")]
sum=0
for i in range(0, len(a)):
    b[i] = int(b[i])
    a[i] = int(a[i])   
sum=0
for i in range(len(a)):
    power=(a[i]-b[i])**2
    sum+=power
    
print(round(sum**0.5, 2))
