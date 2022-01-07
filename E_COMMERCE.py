x = input("ENTER VALUE OF PRODUCT 1:")
y = input("ENTER VALUE OF PRODUCT 2:")
add = int(x) + int(y)
tax = add*0.1
total = add + tax
if total >= 1000:
    total = total - total*0.1
elif total>=500 and total<1000:
    total = total - total*0.07
else:
    pass
print(total)
li = ["Milk,Chocolate,Biscuit,Maggi"]
