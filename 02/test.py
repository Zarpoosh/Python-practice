num = input("enter character:")
floor = int(input("enter number"))

for i in range(floor):
    for j in range(i + 1):
        print(' ' * (floor - i - 1) + num + ' ' * (2 * j) + num)
  
  
  
  
  
  
  
# list=[]  
# floor=int(input())
# num=input()
# list.append(num)
# k = floor - 1
# # outer loop to handle number of rows
# for i in range(0, floor):
    
#     # inner loop to handle number spaces
#     # values changing acc. to requirement
#     for j in range(0, k):
#         print(end=" ")
    
#     # decrementing k after each loop
#     k = k - 1
    
#     # inner loop to handle number of columns
#     # values changing acc. to outer loop
#     for j in range(0, len(list)):
        
#         # printing stars
#         print(list*(i), end="")
    
#     # ending line after each row
#     print("\r")