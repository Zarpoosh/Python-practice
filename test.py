# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Start tag:", tag)
#         for attr in attrs:
#             print("     attr:", attr)

#     def handle_endtag(self, tag):
#         print("End tag  :", tag)

#     def handle_data(self, data):
#         print("Data     :", data)

#     def handle_comment(self, data):
#         print("Comment  :", data)

#     def handle_entityref(self, name):
#         c = chr(name2codepoint[name])
#         print("Named ent:", c)

#     def handle_charref(self, name):
#         if name.startswith('x'):
#             c = chr(int(name[1:], 16))
#         else:
#             c = chr(int(name))
#         print("Num ent  :", c)

#     def handle_decl(self, data):
#         print("Decl     :", data)

# parser = MyHTMLParser()



# def f(**a):
#     print(a)
#     return a["tool"]*a["arz"]

# x=print(arz=25)

# !---------------------

# list=[]
# temp=[]
# for i in range(3):
#     for j in range(2):
#         a= int(input(":"))
#         temp.append(a)
#     list.append(temp)
#     print(list)

# !--------------------------
# def sum(*a):
#     sum=0
#     for item in a:
#      sum+=item
#     return sum

# s=sum(2,3,4,5,6)
# print(s)

# !-----------------------
# a=[2,3,4]
# b=["w", "x", "y", "z"]
# m=zip(a,b)
# print(type(m))
# n=list(m)
# print(n)
# !----------------------
# ch=input(":")
# if ch>="A" and ch<="Z":
#     print("UPPER")
# else:
#     print("lower")

# !-------------------- wrong -------------
# ch=input(":")
# if ch>=65 and ch<=90:
#     print("UPPER")
# else:
#     print("lower")
    
# !---------------------
# chr=input("enter a char:")
# print(f"{chr}:{ord(chr)}")

# !------------------------
# x=int(input("enter number :"))
# a="hello" if x>5 else "bye"
# print(a)
#!----------------------------
# a=[1]+[2]*2+[3]*3
# print(a)
# x,*y,z,r,t,m=a
# print(y*5)
# ! --------------------------
# x=[2,3,4,5,6]
# del x[1:3]
# print(x)
# !--------------------------
# x=[2,3,4,5]
# a,*b,c=x
# print(a,b,c)
# !---------------------------
# x=[2,3,4,5]
# i=x.index(3)
# print(i)
# !--------------------------
# ch=list("Minoo \n Zarpoosh")
# print(ch)
# for i in ch:
#     print(i, end=" ")
# !--------------------------

# چهار عد  ا ز ورودی بگیرد و د. عدد که کم ترین اختلاف را با هم دارن چاپ کند
# a = list(map(int, input("enter 4 numbers : ").split()))

# min_diff = abs(a[0] - a[1])
# min_pair = [a[0], a[1]]

# for i in range(2, len(a)):
#   for j in range(i + 1, len(a)):
#     if abs(a[i] - a[j]) < min_diff:
#       min_diff = abs(a[i] - a[j])
#       min_pair = [a[i], a[j]]

# print("2 numbers with min abs:", min_pair)

# !----------------------------------
# بیشترین اختلاف ار چاپ میکند
# a=[]
# for i in range(4):
#     a.append(int(input()))
# a.sort()
# print(a[0],a[-1])
# !--------------------------
# x=range(0,10,2)
# print(x)
# y=list(x)
# print(y)
# !--------------------------
# a=[2,3]
# b=[4,7]
# c=a+b
# print(c)
# !-------------------------- phone book -------------------------
# phone_numbers={"minoo":"09940" ,"maryam":"7566354", "kimia":"656421" , "dady":"9954648"}
# k=input("Enter name:")
# if k in phone_numbers:
#     print(phone_numbers[k])
# else:
#     print("404 not found!")
#     answer=input("do you want add to note book?(y/n)")
#     if answer=="y":
#         new_number=input(f"what is {k}'s number ?")
#         phone_numbers[k]=new_number
# print(phone_numbers)
# ! ----------------------------------------------
# a = {'x':100, 'y':200}
# b = list(a.items())
# print(b)
# !-----------------------------------
m=[[1,2,3], [4,5,6], [7,8,9]]
c=0
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j] , end="\t")
        if m[i][j] <0:
            c+=1
    print(" ") 
            
sum=0
for i in range (len(m[0])):
    sum+=m[i][0]
print(sum)