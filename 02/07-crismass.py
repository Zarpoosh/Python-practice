# num=input()
# floor=int(input())
# for i in range(floor):
#     print(' '*(floor-i) + num*(i))  

#########################################################
  
  
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

###############################################
# a = [ int(c) for c in input().split(" ")]
# str=input()
# for d in range (len(str)):
#     print(str[d] , end=" ")
    
# x=int(input())
# k = x - 1
# for i in range(0, x):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i+1):
#         # printing stars
#         # print(str[d], end=" ")
#         for d in range (len(str)):
#             print(str[d] , end=" ")
    
#     # ending line after each row
#     print("\r")



# rows = int(input("Enter number of rows: "))

# k = 0

# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end="  ")
   
#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1
   
#     k = 0
#     print()
#######################################################
# str=list(input())
# rows = int(input("Enter the number of rows:"))   
# k = rows - 1   
# j=len(str)
# for i in range(rows):    
#     for j in range(k):    
#         print(end=" ")    
#     k = k - 1       
#     for j in range(i+1):    
#         print(j, end=" ")
#         # print(j% len(str))
#         # for d in range(len(str)):
#         #     print(str[d]+" ", end="") 
#         # #     d+=1 
#         # print("* ", end="") 
            
#     print("")    
    
##########################################################3
# str=list(input())
# rows = int(input(""))   
# k = rows - 1 
# for i in str:
#     # print(i , end=" ")
#     while rows%len(str)>1:
#         print(i , end=" ")

# #############33#########################################
# user_input = input("Enter a string: ")
# triangle = el_saqin_triangle(user_input)
#     # Convert the string to a list of characters
# char_list = list(striuser_inputng)

# # Initialize the triangle list with the first character
# triangle = [char_list[0]]

# # Iterate over the remaining characters
# for i in range(1, len(char_list)):
#     # Concatenate each character with the last element in the triangle
#     new_member = triangle[-1] + char_list[i]
#     triangle.append(new_member)

# # Print the El-Saqin Triangle
# for member in triangle:
#     print(member)
#####################################################################3
# str=input("Enter a string: ")
# rows = int(input(""))   

# # lenght = len(str)
# for i in range(rows):
#     for j in range (rows-i-1):
#         print(" ",end="")
#     for j in range (i+1):
#         print(str[j],end=" ")
#     print()

# str_input = input("Enter a string: ")
# rows = int(input("Enter the number of rows: "))

# # Iterate over the rows
# for i in range(rows):
#     for _ in range(rows - i - 1):
#         print(" ", end="")
#     for j in range(i + 1):
#         print(str_input[j], end=" ")
#     print()
    
    
#         @
#        @ # 
#       @ # * 
#      @ # * @ 
#     @ # * @ # 
#    @ # * @ # *
#   @ # * @ # * @
#         |


# str = input("Enter a string: ")
# rows = int(input("Enter the number of rows: "))

# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ", end="")
#     for j in range(i + 1):
#         if j == i:  # Add '*' at the end of each row
#             print(str[j] + " *", end="")  # Add space between characters
#         else:
#             print(str[j] + " ", end="")  # Add space between characters
#     print()




# str = input("Enter a string: ")
# rows = int(input("Enter the number of rows: "))

# str_length = len(str)  # Length of the string

# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ", end="")
#     for j in range(i + 1):
#         char_index = j % str_length  # Wrap around the characters using modulo
#         if j == i:  # Add '*' at the end of each row
#             print(str[char_index] + " *", end="")  # Add space between characters
#         else:
#             print(str[char_index] + " ", end="")  # Add space between characters
#     print()
         
         
         
         
str = input("Enter a string: ")
rows = int(input("Enter the number of rows: "))

str_length = len(str) 
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        char_index = j % str_length  
        print(str[char_index] + " ", end="") 
    for j in range(rows - i - 1):
        print(" ", end="")
    print()
for j in range(rows - i - 1):
    print(" ", end="")
    print(" " +"|")  