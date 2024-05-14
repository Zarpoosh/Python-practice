# def count_falling_stones(stones, hit_stone):
#   """
#   این تابع تعداد سنگ هایی که پس از ضربه زدن به سنگ با شماره hit_stone 
#   روی زمین می افتند را محاسبه می کند.

#   Args:
#     stones: لیستی از اعداد 1 تا 7 که نشان دهنده ترتیب قرارگیری سنگ ها از 
#            پایین به بالا است.
#     hit_stone: شماره سنگی که به آن ضربه زده می شود.

#   Returns:
#     تعداد سنگ هایی که روی زمین می افتند.
#   """

#   falling_stones = 0
#   for stone in stones:
#     if stone <= hit_stone:
#       falling_stones += 1
#   return falling_stones

# # خواندن ورودی
# stones = list(map(int, input().split()))
# hit_stone = int(input())

# # محاسبه تعداد سنگ های در حال سقوط
# falling_stones = count_falling_stones(stones, hit_stone)

# # چاپ خروجی
# print(falling_stones)



user_input = input("Enter 7 numbers separated by spaces (any order): ")

numbers = [int(num) for num in user_input.split()]

if len(numbers) != 7:
  print("Invalid input. Please enter exactly 7 numbers.")
else:
  compare_number = int(input("Enter a number from 1 to 7: "))

  if compare_number not in range(1, 8):
    print(f"Invalid input. Please enter a number between 1 and 7.")
  else:
   
