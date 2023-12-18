# give the price of product
price=float(input())

# give the off of rpoduct
Discounted=int(input())

# apply discount
result=price-price*(Discounted/100)


x=round(result,2)
# print the product
print(x)
