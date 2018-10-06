from Deal import Player, Dealer

# casinos use a six-deck game (312 cards)
# Ace - 1 or 11
# 2, 3, 4, 5, 6, 7, 8, 9, 10
# All face cards = 10  -> J, Q, K

# Game starts with a bet limit b/w $2 - $500
# Regular wins, player earns as much as they bet
# BlackJack wins then player earns 1.5x their bet amount
# Push (Tie/Draw) - Player keeps their bet. Loses nothing

# BlackJack is an Ace with any 10pt card and is an automatic win unless dealer also has BJ

# asking to play a game
while input("\n\t\t\tPlay BlackJack?(y/n): ") == 'y':
    # If cannot find save file then write a new one
    try:
        file = open("blackjack.txt", "r+")
        my_list = file.read().splitlines()
        print("\t\t\t\nContinuing game...\n")

        game_record = [0, 0, 0, 0]  # Holds variables - Wins, Losses, BlackJacks, and Busts
        bank = 0
        i = 0
        for line in my_list:
            if i == 0:
                print("Bank: $%s" % line)
                bank = float(line)
            elif i == 1:
                print("Wins: %s" % line)
                game_record[0] = int(line)
            elif i == 2:
                print("Losses: %s" % line)
                game_record[1] = int(line)
            elif i == 3:
                print("BlackJacks: %s" % line)
                game_record[2] = int(line)
            else:
                print("Busts: %s\n" % line)
                game_record[3] = int(line)
            i += 1
        file.close()
    except FileNotFoundError:
        file = open("blackjack.txt", "w")
        print("\t\t\tNew Game")
        game_record = [0, 0, 0, 0]  # Holds variables - Wins, Losses, BlackJacks, and Busts
        bank = 1000.00

    if bank < 100:
        print("Elon Musk donated $1000 for your gambling addiction")
        bank += 1000

    bet = float(input("Enter bet amount. Can be between $2 and $500.\nCurrently you have $%.2f\n" % bank))

    while bet < 2.00 or bet > 500.00:
        bet = float(input("Enter bet amount. Can be between $2 and $500.\nCurrently you have $%.2f\n" % bank))

    print("\n\t\tYou bet: %.2f" % bet)

    print("\t\t########## GAME START ##########\n")

    # Initialize hands
    player_hand = Player()
    dealer_hand = Dealer()

    # Overwrite current game file with new game_record
    file = open("blackjack.txt", "w")

    file.write("%.2f" % player_hand.starting_hands(game_record, dealer_hand, player_hand, bank, bet))

    for num in game_record:
        file.write("\n%s" % num)
    file.close()


print("\t\t\tThanks For Playing!")


