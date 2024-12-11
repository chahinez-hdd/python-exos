people= int(input("how many people needs a ride"))

taxiCapacity = int(input("how many people fits in one taxi?"))

nb = people // taxiCapacity

if people%taxiCapacity== 0:
    print(f"Number of taxis needed: { int(nb)}")
else:
    print(f"Number of taxis needed: { int(nb)+1}")