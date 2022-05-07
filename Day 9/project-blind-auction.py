import art
import os


def clearConsole():
    command = 'clear'
    os.system(command)


print(art.logo)
print("Welcome to the secret auction program")

# Create a list to place all bidders
all_bidders = []

# Create function to add bidder's info to the list


def add_new_bidder(new_bidder, new_bid):
    bidders = {}
    bidders["Name"] = new_bidder
    bidders["Bid"] = new_bid
    all_bidders.append(bidders)


end_of_auction = False
while not end_of_auction:
    # Ask the person for a name and a bid
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    add_new_bidder(name, bid)

    auction = input(
        "Are there any other bidder? Type 'yes' or 'no'. \n").lower()

    # Figure out if there are other people willing to bid
    if auction == "yes":
        clearConsole()
    else:
        end_of_auction = True

# initialize prev_amt to other bidders' bid to see which is higher
prev_amt = 0
for bids in all_bidders:
    if bids["Bid"] > prev_amt:
        prev_amt = bids["Bid"]
        winner_name = bids["Name"]
        winner_bid = bids["Bid"]

# Confirm the winner
print(f"The winner is {winner_name} with a bid of ${winner_bid}")
