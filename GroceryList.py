grocerylist = ["Apple", "Banana", "Pear", "Sausage", "Lotion", "Vegetables"]
shoppingcart= ["Apple", "Banana", "Pear", "Sausage", "Lotion", "Vegetables"]

count = 0

for x in grocerylist:
    for y in shoppingcart:
        if x == y:
            count += 1
            continue

if count == len(grocerylist):
    print("klaar met shoppen!")
else:
    print("continue shopping!")
