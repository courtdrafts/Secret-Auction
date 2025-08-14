
from replit import clear
from art import logo

r = "yes"
bidders = {}
maxBid = 0
bName = ""

while r != "no":
    
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bidV = float(input("What's your bid?: $ "))
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    r = other
    bidders[name] = bidV
    clear()
    
    for key in bidders:
        if maxBid < bidders[key]:
            bName = key
            maxBid = bidders[key]


print(f"The winner is {bName} with a bid of {maxBid}")    