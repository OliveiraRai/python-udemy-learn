### Secret Auction 
print("Welcome to the Secret Auction program.")
isMore_bidders = True
dict = {}
winner = ""
best_bid = 0
while isMore_bidders == True:
    name = input("What is your name? ")
    while True:
        try:
            bid = int(input("What is your bid? $"))
            if isinstance(bid, int):
                break
        except ValueError:
            print("Please, use only numbers here.")
            print("")
    dict[name] = bid
    while True:
        question = input("Are there any more bidders? Type 'yes' or 'no'.\n  ").lower()
        if question == 'yes' or question == 'no':
            break
        else:
            print("")
            print("Please, type 'yes' or 'no'.")
            print("")
    if question == 'yes':
        print("\n" * 25)
        continue
    elif question == 'no':
        print("")
        for key in dict:
            if dict[key] > best_bid:
                best_bid = dict[key]
                winner = key
        print(f"{winner} won! The bid was ${best_bid}.")
        isMore_bidders = False
            