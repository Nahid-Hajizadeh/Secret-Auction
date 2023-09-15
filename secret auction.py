import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''

print(logo)

bidder_dictionary = {}
winner_name = ""
highest_bid = 0
bidding_finished = False
while not bidding_finished:
    print("Welcome to the 'Secret Auction' program ")
    name = input("Enter your name : ")
    bid = int(input("What is your bid? : $"))
    bidder_dictionary[name] = bid
    if bid > highest_bid:
        winner_name = name
        highest_bid = bid
    is_finished = input("Is the auction finished? Type 'yes' or 'no'.\n")
    if is_finished == "yes":
        os.system('cls')
        print(f"The winner is {winner_name} with a bid of ${highest_bid}")
        bidding_finished = True
    else:
        # Clear te Output in the Console.
        os.system('cls')

# If you want the terminal to emulate your OSs terminal, you have to edit the 'Run/Debug Configuration' and tick the
# box 'Emulate terminal in output console'. Then os.system("cls") will clear the screen on Windows and os.system(
# "clear") on unix
