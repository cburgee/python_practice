auction_status = False
bidders = {}
highest_bid = 0
highest_bidder = ""
bidder_name = input("What is your name?\n")
bid_amount = int(input("What is your bid? \n$"))
bidders[bidder_name] = bid_amount
do_continue = input("Would you like to add another bidder? 'yes' or 'no'\n")

if do_continue.lower() == "yes":
    auction_status = True

while auction_status == True:
    bidder_name = input("What is your name?\n")
    bid_amount = int(input("What is your bid? \n$"))
    bidders[bidder_name] = bid_amount
    do_continue = input("Would you like to add another bidder? 'yes' or 'no'\n")
    if do_continue.lower() == "no":
        auction_status = False

for k in bidders:
    if bidders[k] > highest_bid:
        highest_bid = bidders[k]
        highest_bidder = k

print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")
