# numbers = []
# for i in range(10):
#     number = input()
#     numbers.append(number)

# sum_columns = [0] * 11

# for number in numbers:
#     for i in range(11):
#         digit = int(number[i])
#         sum_columns[i] += digit

# result = 1
# for sum_column in sum_columns:
#     result *= sum_column

# print(result)

# ----------------------------------------------------------------

# numbers = []
# for i in range(3):
#     number = input()
#     while len(number) != 4 or not number.isdigit():
#         print("Invalid input. Please enter an 4-digit number.")
#         number = input()
#     numbers.append(number)

# sum_columns = [0] * 4

# for number in numbers:
#     for i in range(4):
#         digit = int(number[i])
#         sum_columns[i] += digit

# result = 1
# for sum_column in sum_columns:
#     result *= sum_column

# print(result)

# -------------------------------------------------------------

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]   
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j])        
print(matrix)
