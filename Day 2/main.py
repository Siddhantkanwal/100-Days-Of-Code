print("Welcome to the tip calculator")
a=float(input("What was the total bill?\t"))
b=int(input("What percentage tip would you like to give ? 10,12, or 15?\t"))
c=int(input("How many people to split the bill?\t"))
d=0
e=0
e=(a*b)/100
d=round((a+e)/c,2)
print(f"Each person should pay {d}")
