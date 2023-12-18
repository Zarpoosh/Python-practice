# اعداد بین ۱ تا ۱۰ را چاپ کند؟
# for i in range (1, 10):
#     print(i)

# #############################

# همه اعداد فرد بین ۱۰۰ تا ۲۰۰ را چاپ کند؟
# for i in range(101 , 200):
#     if i%2==1:
#         print(i)

#################################

# ?????
# x =int(input("enter first number:"))
# y =int(input("enter second number:"))
# if x>y:
#     for i in range (x,y+1):
#         print(i)
# else:
#     for i in range(y, x+1):
#         print(i)

################################

# ۱۰ عدد را بگیره و کوچکترین عدد رو چاپ کنه؟
# min=float(input("enter number:"))
# for i in range(9):
#     a=float(input("enter new number :" ))
#     if a<min:
#         min=a
#         print(a)

#############################
# یک عدد صحیح را بگیره و مشخص کنه اول است یا خیر؟؟؟؟
# f=0
# n=int(input("enter number"))
# for i in range(2,n):
#     if n%n==0:
#         f=1
#     if f==0:
#         print("prime")
#     else:
#         print("not prime")
        
##############################

# یه عدد صحیح بگیره و اعدادی که بهش بحش یرن رو چاپ کنه؟
# n = int(input("enter number:"))
# for i in range(1, n+1):
#     if n%i==0:
#         print(i)
        
############################

# یه عدد صحیح بگیره و برعکس آن را چاپ کنه؟
# n=int(input("enter number:"))
# a=0
# while n!=0:
#     r=n%10
#     a=(a*10)+r
#     n=n//10
# print(a)

##########################

# جدول ضرب ۹*۹ را چاپ کند؟
# for i in range(1,10):
#     for j in  range(1, 10):
#         print(i*j , end=" ")
#     print(" ")

#########################

# ۵ عدد از وزودی بگیره و میانگین اونا رو چاپ کنه؟
# sum=0
# for i in range(5):
#     a=float(input("enter number:"))
#     sum=sum+a
    
# avg=sum/5
# print(f"avg={avg}")

#######################

# تا وقتی نام درست را نگرفته بپرسد؟
# name=input("enter name:")
# while name !="minoo":
#     print("Na")
#     name=input("enter name:")
# print("Are dorost Gofti !")

#######################3

# تا وقتی ۵ عدد منفی از ورودی نگرفته همش عدد بگیرد؟
# count=0
# while count<5:
#     a=float(input("enter number:"))
#     if a<0:
#         count=count+1
# print(count)

##########################

# ستاره ها را مربعی چاپ کند؟
# n=int(input("enter number:"))
# for i in range(1,n+1):
#     for j in  range(1, n+1):
#         print("*", end=" ")
#     print("")
    

##########################3

# ستاره ها را مثلثی چاپ کند؟
# n=int(input("enter number:"))
# for i in range(1,n+1):
#     for j in  range(1, i+1):
#         print("*", end=" ")
#     print("")
    
#############################

# ستاره ها را مثلثی برعک چاپ کند؟
# n=int(input("enter number:"))
# for i in range(1,n+1):
#     for j in  range(i, n+1):
#         print("*", end=" ")
#     print("")

# ##############################

# حروف اول و اخر کلمه را بگیره بهم بچشبونه؟
# word=input("enter word:")
# m=len(word)
# s=word[0] + word[m-1]
# print(s)

#################################

# کلمه ای بگیره جدا جدا بنویسه؟
# word=input("enter word:")
# m=len(word)
# for i in range(m):
#     print(word[i] ,end=" ")


################################3

#کلمه رو بگیره حروف صدا دارشو حذف کنه؟
# word=input("enter word:")
# m=len(word)
# for i in range(m):
#     if word[i]!="a" and word[i]!="i" and word[i]!="o" and word[i]!="u" and word[i]!="e" :
#         print(word[i], end="")

####################################3]

# پیدا کردن رمز؟
# from random import randint
# alphabet="abcde"
# password=""
# m=0
# while password !="bde":
#     m=m+1
#     password=""
#     for i in range(3):
#         n=randint(0, len(alphabet)-1)
#         password=password+alphabet[n]
#     print(password)

# print("Ramz Peyda Shod!")
# print(m)

##################################3333

# string = "Welcome to SabzDanesh.com site!"
# i = 0
# for char in string:
#     i+=1
# print("Lenght is: " + str(i))


