# import math

# # Set the size of the heart
# size = 10

# # Loop to print the rows
# for y in range(-size, size + 1):
#     # Loop to print the columns
#     for x in range(-2 * size, 2 * size + 1):
#         # Calculate the distance from the current point to the origin
#         dist = math.sqrt(x**2 + y**2)
        
#         # Check if the current point is within the heart shape based on the distance
#         if dist <= size * math.sin(math.atan2(y, abs(x))) or (y >= 0 and dist <= size * 0.6):
#             print("❤️", end="")
#         else:
#             print("  ", end="")
#     print()


# def print_heart_shape(size):
#     for y in range(-size, size + 1):
#         for x in range(-2 * size, 2 * size + 1):
#             # Calculate the distance from the current point to the origin
#             dist = (x / size)**2 + (y / (size * 0.6))**2 - 1
            
#             # Check if the current point is within the heart shape based on the distance
#             if dist <= 0.01:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
        
#     print_heart_shape(5)
