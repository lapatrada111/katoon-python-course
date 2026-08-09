prices = []

print("Enter prices of 6 items:")
for i in range(6):
    price = int(input("Item " + str(i + 1) + ": "))
    prices.append(price)

print("")
budget = int(input("Enter total budget: "))
print("")

current_total = 0
bought_items = []

for i in range(6):
    price = prices[i]
    if current_total + price <= budget:
        current_total = current_total + price
        bought_items.append(price)
        print("Item " + str(i + 1) + " = " + str(price) + " -> buy")
    else:
        print("Item " + str(i + 1) + " = " + str(price) + " -> cannot buy")
    print("Current total = " + str(current_total))
    print("")

remaining = budget - current_total
print("Bought items: " + str(bought_items))
print("Total spent: " + str(current_total))
print("Remaining budget: " + str(remaining))
