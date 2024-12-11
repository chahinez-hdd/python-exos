totalAmount= int(input("Total amount: "))
nbItems= int(input("Number of items: "))
day=input("Day of the week: ")

moreThanFive=False
if nbItems>5:
    moreThanFive=True

if day=='Saturday' or day =='Sunday':
    if(moreThanFive):
        disc=totalAmount*0.25
        amount=totalAmount-disc
    else:
        disc=totalAmount*0.2
        amount=totalAmount-disc
else:
    if(moreThanFive):
        disc=totalAmount*0.15
        amount=totalAmount-disc
    else:
        disc=totalAmount*0.1
        amount=totalAmount-disc

print(f"Total price after discount: {amount} dinars")