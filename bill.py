import os.path

filename = "Bill.csv"

print("""Welcome to Sanszee Sandwich Hub!!!
Menu
1.  Toasted Bread                   $1.99 
2.  Plain cheese sandwich           $2.35
3.  Mustardy Cheese sandwich        $2.50
4.  Traditional American Sandwich   $5.99
5.  Schezwan Rice Sandwich          $2.99
6.  Spaghetti Sandwich              $4.99
7.  French Fry                      $0.99
8.  Cheese Burger                   $2.50
9.  Veg Burger                      $2.45""")

choix = -1
item = []
i = 0
qty = 0
gtotal = 0

if os.path.exists(filename):
    os.remove(filename)

with open(filename, "a") as fh:
    fh.write("Sanszee Sandwich hub \n")

mm=["item","price","Qty","Tprice"]

with open(filename, "a") as fh:
    fh.write(",".join(map(str, mm)) + "\n")

while choix != 0:
    i += 1
    choix = int(input("Item no from 1-9 (enter 0 to finish): "))
    if choix == 1:
        qty = int(input("Quantity = "))
        if qty!=0:
            item = ["Toasted Bread", 2.50, qty, 1.99 * qty]
    elif choix == 2:
        qty = int(input("Quantity = "))
        if qty!=0:
            item = ["Plain cheese sandwich", 2.35, qty, 2.35 * qty]
    elif choix == 3:
        qty = int(input("Quantity = "))
        if qty!=0:
            item = ["Mustardy Cheese sandwich", 1.99, qty, 1.99 * qty]
    elif choix == 4:
        qty = int(input("Quantity = "))
        if qty!=0:
            item = ["Traditional American Sandwich", 5.99, qty, 5.99 * qty]
    elif choix == 5:
        qty = int(input("Quantity = "))
        if qty!=0:
            item = ["Schezwan Rice Sandwich", 2.99, qty, 2.99 * qty]
    elif choix == 6:
        qty = int(input("Quantity = "))
        if qty!=0:
            item = ["Spaghetti Sandwich", 4.99, qty, 4.99 * qty]
    elif choix == 7:
        qty = int(input("Quantity = "))
        if qty!=0:
            item = ["French Fry", 0.99, qty, 0.99 * qty]
    elif choix == 8:
        qty = int(input("Quantity = "))
        if qty!=0:
            item = ["Cheese Burger", 1.99, qty, 1.99 * qty]
    elif choix == 9:
        qty = int(input("Quantity = "))
        if qty!=0:
            item = ["Veg Burger", 2.45, qty, 2.45 * qty]
    else:
        break
    
    gtotal += item[3]
    
    with open(filename, "a") as fh:
        fh.write(",".join(map(str, item)) + "\n")
    
    item.clear()

with open(filename, "a") as fh:
    fh.write("Grand total = " + str(gtotal))

print("Order details saved in", filename)
