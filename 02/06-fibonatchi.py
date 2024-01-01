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



from collections import OrderedDict
a={}
b=[]
for j in range(3):
    n=int(input())
    b.append(n)
c=0
m=[]

for number in b:
    v=0
    m.clear()
    x=False
    for h in range(m[1], len(m)-1):
        for u in range(2,h):
            if h%u==0:
                x=True
        if x==False:
            v+=1
    a[v]=number
    if v>c:
        c=v
print(a[c], c)