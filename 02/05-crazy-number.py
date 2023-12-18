# x=[]
# for i in range(4):
#     numbers =float(input())
#     x.append(numbers)
# # print(x)
# var=0
# for i in range(len(x)):
#     result=x[i]**i
#     var+=result
# print(round(var ,2))


# # x=[]
# numbers =float(input())
# # x.append(numbers)
# # print(x)
# var=0
# for i in range(len(numbers)):
#     result=numbers[i]**i
#     var+=result
# print(round(var ,2))

# ########################################
# x=input(float())
# y=" ".join([x])
# # x=[input1,input2,input3,input4]
# array=y.split(" ")
# for i in range(0, len(array)):
#     array[i] = float(array[i])
#     # print(array)
#     print(i, end=" ")
    
#     var=0
#     result=array[i]**i
#     var+=result
# print(round(var ,2))

#############################################


x=input()
y=" ".join([x])
# x=[input1,input2,input3,input4]
array=y.split(" ")
sum=0
for i in range(0, len(array)):
    array[i] = float(array[i])
    # print(array, end=" ")
var=0
for i in range(len(array)):
    result=array[i]**i
    var+=result
print(var)


#######################################

# def calculate_sum(numbers):
#     total = 0
#     for i in range(len(numbers)):
#         total += numbers[i] ** i
#     return total

# # Example usage
# numbers_list = [2, 3, 4, 5]
# result = calculate_sum(numbers_list)
# print("The sum is:", result)