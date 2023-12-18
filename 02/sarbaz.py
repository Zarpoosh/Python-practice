# a = [int(c) for c in input().split()]
# sequence = []
# longest = []
# for num in a:
#     if not sequence or num > sequence[-1]:
#         sequence.append(num)
#     else:
#         if len(sequence) > len(longest):
#             longest = sequence.copy()
#         sequence = [num]

# if len(sequence) > len(longest):
#     longest = sequence.copy()

# print( longest)

#########################################################################3

# a = [int(c) for c in input("Enter a list of integers: ").split()]

# # Variables to keep track of the current sequence and the longest sequence
# sequence = []
# longest = []

# for num in a:
#     # If the sequence is empty or the current number is greater than the previous number
#     # add it to the sequence
#     if not sequence or num > sequence[-1]:
#         sequence.append(num)
#     else:
#         # If the current sequence is longer than the longest sequence found so far, update it
#         if len(sequence) > len(longest):
#             longest = sequence.copy()
#         sequence = [num]

# # Check if the last sequence is the longest
# if len(sequence) > len(longest):
#     longest = sequence.copy()

# print("Longest sequence:", longest)
########################################################################
# print(a)
# for i in range(len(a)):
#     if a[i]-a[i-1]== -1 :
#         print(a[i])

# a = [ int(c) for c in input().split()]
# count=0
# for i in range(len(a)):
#     b= a[i] - a[i - 1] 
#     if b==1:
#         # print(b)
#         count+=1  
#     else:
#         break
        
        
# print(count)



# a = [ int(c) for c in input().split()]
# count=0
# b=[]
# for i in range(len(a)):
#     b= a[i] - a[i - 1] 
#     if b<2:
#         count+=1
      
# print(count)



a = [int(c) for c in input().split()]
current = [a[0]]
longest = [a[0]]

for i in range(1, len(a)):
    if a[i] == a[i-1] + 1:
        current.append(a[i])
    else:
        if len(current) > len(longest):
            longest = current.copy()
        current = [a[i]]

if len(current) > len(longest):
    longest = current.copy()

for i in range(len(longest)):
    print(longest[i] , end=" ")
    
    