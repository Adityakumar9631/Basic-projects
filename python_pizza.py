print("Thank you for choosing Python Pizza Deliveries")
size = input("What size pizza do you want ? S,M or L:  ")
add_pepperoni = input("Do you want pepperoni ? Y/N :  ")
extra_cheese = input("Do you want extra cheese ? Y/N : ")
if(size =="S"):
    price=15
elif(size =="M"):
    price=20
elif(size=="L"):
    price=25
if(add_pepperoni =="Y"):
    cost=2
elif(add_pepperoni =="N"):
    cost=0
if(extra_cheese =="Y"):
    amount=1
elif(extra_cheese =="N"):
    amount=0
total_bill=price +cost+amount
print("Your final bill in dollor is: ",total_bill)
