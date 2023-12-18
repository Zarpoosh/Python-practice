def calculate_discount(price, discount):
  discount_fraction = discount / 100
  discounted_price = price * (1 - discount_fraction)
  # print(discounted_price )
  
  return round(discounted_price, 2)

price = float(input())

discount = int(input())

discounted_price = calculate_discount(price, discount)

print("قیمت تخفیف داده شده کالا:", discounted_price)
################################################################
# give the worth of product
worth=float(input("enter your price:"))

# give the off of product
Discounted=int(input("enter your off:"))

off=worth*(Discounted/100)

# apply discount
outcome=worth-off

x=round(outcome,2)
# print the product
print(x)
