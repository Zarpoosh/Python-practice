num=int(input())
fib_numbers=[]
num1, num2 = 0, 1
for i in range (num):
    fib_numbers.append(num1)
    num1, num2 = num2, num1 + num2
for i in range (len(fib_numbers)):
    print(fib_numbers[i] , end=" ")

# second way with function
# def fibonacci_sequence(n):
#     sequence = []
#     num1, num2 = 0, 1
#     for _ in range(n):
#         sequence.append(num1)
#         num1, num2 = num2, num1 + num2
#     return sequence

# num = int(input("عدد را وارد کنید: "))
# fib_sequence = fibonacci_sequence(num)
# print(fib_sequence)