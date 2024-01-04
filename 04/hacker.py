# example_matrix = []
# print(":")

# for i in range(3): 
#     r = []
#     for j in range(2): 
#         r.append(int(input()))
#     example_matrix.append(r)

# column_sums = [0] * 2  

# for i in range(3):
#     for j in range(2):
#         print(example_matrix[i][j], end=" ")

#         column_sums[j] += example_matrix[i][j]

#     print()

# result = column_sums[0] * column_sums[1]
# print("Result:", result)

# -------------------------------------------------
# for i in range(3):
#     a = [ int(c) for c in input().split(" ")]
    




# Initializing the matrix
# example_matrix = []

# print("Please enter the numbers:")

# # For user input
# for i in range(3):  # This for loop is used to read 3 lines of input
#     num = input().strip()

#     # Check if the number has exactly 4 digits
#     if len(num) != 4:
#         print("Please enter a 4-digit number.")
#         continue

#     # Convert each digit of the number to integer and append to the matrix
#     a = [int(digit) for digit in num]
#     example_matrix.append(a)

# # Printing the matrix given by the user
# column_sums = [0] * len(example_matrix[0])  # Initialize a list to store the sums of each column

# for i in range(len(example_matrix)):
#     for j in range(len(example_matrix[i])):
#         print(example_matrix[i][j], end=" ")

#         # Add the value to the corresponding column sum
#         column_sums[j] += example_matrix[i][j]

#     print()

# # Multiply the sums of each column together
# result = 1  # Initialize the result to 1
# for sum in column_sums:
#     result *= sum

# print("Result:", result)


# temp=[]
# for i in range(3):
#      a = [ int(c) for c in input().split(" ")]
#      temp.append(a)
# print(temp)
# for j in range(len(temp)):
#      print(j)

# list=[]
# temp=[]
# for i in range(3):
#      a = int(input()) 
#      temp.append(a)
# print(temp)
     
# list=[]
# temp=[]

# for i in range(3):
#     a = input()
#     temp.append(a)
# # print(len(temp))
# # print(temp)
# for j in range(temp):
#     print(j)



# # Take input from the user
# num1 = input("Enter a 4-digit number: ")
# num2 = input("Enter another 4-digit number: ")
# num3 = input("Enter one more 4-digit number: ")

# # Initialize variables to store the sum of each column
# sum_column_1 = 0
# sum_column_2 = 0
# sum_column_3 = 0
# sum_column_4 = 0

# # Add the numbers of each column together
# for i in range(4):
#     digit1 = int(num1[i])
#     digit2 = int(num2[i])
#     digit3 = int(num3[i])

#     sum_column_1 += digit1
#     sum_column_2 += digit2
#     sum_column_3 += digit3
#     sum_column_4 += digit1 + digit2 + digit3

# # Multiply the sums of the columns
# result = sum_column_1 * sum_column_2 * sum_column_3 * sum_column_4

# # Display the result
# print("The result is:", result)



# Take input from the user
numbers = []
for i in range(3):
    number = input("Enter an 11-digit number: ")
    numbers.append(number)

# Initialize variables to store the sum of each column
sum_columns = [0] * 4

# Add the numbers of each column together
for number in numbers:
    for i in range(4):
        digit = int(number[i])
        sum_columns[i] += digit

# Multiply the sums of the columns
result = 1
for sum_column in sum_columns:
    result *= sum_column

# Display the result
print("The result is:", result)