print("START TICKETING")
print("What is your height in cm?")
height=int(input())
if(height>120):
    print("YOU ARE ELIGIBLE FOR RIDE")
    print("What is your age?")
    age=int(input())
    print("Do you want photos? ")
    photo=input()
    if(age<12):
        cost=5
        if(photo=="yes"):
            money=3
        else:
            money=0
    elif(12<=age<=18):
        cost=7
        if(photo=="yes"):
            money=3
        else:
            money=0
        
    elif(age>18):
        cost=12
        if(photo=="yes"):
            money=3
        else:
            money=0
else:
    print("YOU ARE NOT ELIGIBLE FOR RIDE")
total_bill= cost + money
print("Total Bill For Your Ride Is In Dollor:  " ,total_bill)
    
