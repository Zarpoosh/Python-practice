# operator = input().upper()
# num1 = int(input())
# num2 = int(input())

# if operator == "ADD":
#     result = num1 + num2
# elif operator == "SUB":
#     result = num1 - num2
# elif operator == "MUL":
#     result = num1 * num2
# elif operator == "DIV":
#     if num2 != 0:  # Check for division by zero
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero is not allowed"
# elif operator == "MOD":
#     result = num1 % num2
# elif operator == "POW":
#     result = num1 ** num2
# else:
#     result = "Invalid operator"

# print("Result:", round(result))


operator = input().upper()
num1 = int(input())
num2 = int(input())

if operator == "ADD":
   print(num1 + num2)
elif operator == "SUB":
    print(num1 - num2)
elif operator == "MUL":
    print(num1 * num2)
elif operator == "DIV":
       print(round(num1 / num2))
elif operator == "MOD":
     print(num1 % num2)
elif operator == "POW":
    print(num1 ** num2)