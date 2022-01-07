option = True
data = {}
def update(data):
    item_name = input("ENTER NAME:")
    item_quantity = input("ENTER QUANTITY:")
    data[item_name] = item_quantity
def show(data):
    print("showing items...")
    for i, j in data.items():
        print(i, j)
def search(data,key):
    return data.get(key)
while option:
    print("1.Update items")
    print("2.Show items")
    print("3. Search items")
    print("4. Exit")
    choice = input("ENTER OPTION:")
    if choice == "1":
        update(data)
    elif choice == "2":
        show(data)
    elif choice == "3":
        key=input("ENTER the item to be searched: ")
        print(search(data,key))
    elif choice == "4":
        option = False