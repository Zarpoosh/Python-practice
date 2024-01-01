# import math

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# def count_prime_divisors(n):
#     count = 0
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0 and is_prime(i):
#             count += 1
#     return count

# # Take 5 numbers as input
# numbers = []
# for _ in range(2):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# max_num = None
# max_divisors = 0

# # Find the number with the highest prime divisor
# for num in numbers:
#     divisors = count_prime_divisors(num)
#     if divisors > max_divisors:
#         max_divisors = divisors
#         max_num = num
#     elif divisors == max_divisors and (max_num is None or num > max_num):
#         max_num = num

# print(f"The number with the highest prime divisor is {max_num}.")
# print(f"It has {max_divisors} divisors of prime numbers.")




# from collections import defaultdict

# def find_first_divisor_and_count(number):
#     first_divisor = 0
#     divisor_count = 0
#     for i in range(2, number):
#         if number % i == 0:
#             first_divisor = i
#             divisor_count = 1
#             for j in range(2, first_divisor):
#                 if first_divisor % j == 0:
#                     divisor_count += 1
#                     break
#             break
#     return first_divisor, divisor_count

# a = defaultdict(int)
# b = []

# for j in range(3):
#     n = int(input())
#     b.append(n)

# c = 0

# for number in b:
#     first_divisor, divisor_count = find_first_divisor_and_count(number)
#     a[divisor_count] = max(a[divisor_count], number)
#     if divisor_count > c:
#         c = divisor_count

# print(a[c], c)

from collections import defaultdict

a = defaultdict(int)
b = []

for j in range(3):
    n = int(input())
    b.append(n)

c = 0

for number in b:
    first_divisor = 0
    divisor_count = 0
    v = 0
    for i in range(2, number):
        if number % i == 0:
            first_divisor = i
            divisor_count += 1
            is_prime = True
            for j in range(2, first_divisor):
                if first_divisor % j == 0:
                    is_prime = False
                    break
            if is_prime:
                v += 1

    a[v] = max(a[v], number)
    if v > c:
        c = v

print(a[c], c)

