str = input()
rows = int(input())

str_length = len(str) 
for i in range(rows):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(i + 1):
        char_index = j % str_length  
        print(str[char_index] + " ", end="") 
    for j in range(rows - i - 1):
        print(" ", end="")
    print()
for j in range(rows):
    print(" ", end="")
print("|")  