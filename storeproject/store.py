stock=600
shoes_sold=500
target=500

target_hit= shoes_sold==target

print("Hit shoes sales target: ")
print(target_hit)

current_stock=stock-shoes_sold
in_stock =current_stock!=0
print("shoes in stock :", in_stock)
