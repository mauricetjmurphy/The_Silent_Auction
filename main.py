import operator

print("Hello, welcome to the secret auction\n")
bids = {}

def take_bid(turn, name, bid):
    newbids = {}
    newbids[name] = bid
    bids.update(newbids)

def calc_bids():
    winner = max(bids, key=bids.get)
    print(f"Congratulations {winner.capitalize()}, you are the winner.")

while True:
    turn = input("Would you like to bid? Please enter 'Yes' or 'No'\n").lower()
    if turn != 'yes' and turn != 'no':
        print("Thats not an answer!")
        continue
    if turn == 'no':
        if bool(bids) == False:
            break
        else:
            calc_bids()
            break
    name = input("Please enter your name to place a bid.\n").lower()
    bid = input("Please enter the amount you wish to bid.\n").lower()
    take_bid(turn, name, bid)
