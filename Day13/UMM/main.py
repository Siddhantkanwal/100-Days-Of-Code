from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

dict={}
biding=False

def hight(biding):
  highest=0
  winner=""
  for bidder in biding:
    bid_a=biding[bidder]
    if bid_a>highest:
      highest=bid_a
      winner=bidder
  print(f"The winner f{winner} with a bid of ${highest}")

while not biding:
  name =input("What is your name")
  bid =int(input("what is your bid"))
  dict[name]=bid
  s_c=input("Are there any other bidders? Tupe 'yes 'or' no'")
  if s_c=="no":
    biding=True
    hight(dict)
  elif s_c=="yes":
    clear()