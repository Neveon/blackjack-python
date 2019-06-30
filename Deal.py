import random


class Player:

    def __init__(self):
        self.playing_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.hand = []
        self.total = 0

    def starting_hands(self, game_record, dealer, player, bank, bet):
        # prints hand and stores, in hand variable, the first two playing cards dealt
        for num in range(0, 2):
            x = random.randint(0, len(self.playing_cards) - 1)  # random integer from 0 - 12 (randint includes 12)
            self.hand.append(self.playing_cards[x])  # appends random card to hand variable

        print("Your hand:\n%s\n%s\n" % (self.hand[0], self.hand[1]))
        # dealer shows hand
        dealer.starting_hands()

        # for each card in the hand, we add the equivalent value of the card
        for card in self.hand:
            try:
                if card == 'A':
                        # Aces can be 1 or 11. Pocket Aces are equivalent to 11.
                        if self.total + 11 > 21:
                            self.hand[self.hand.index(card)] = 1
                            self.total += 1
                        else:
                            self.total += 11
                elif card in 'JQK':
                    self.total += 10
            # If the card is a number it will output a TypeError from the above
            except TypeError:
                self.total += card

        # Auto stand at BlackJack
        if self.total == 21:
            print("BlackJack!")
            game_record[2] += 1
            # reveals dealer card
            return dealer.reveal_hole_card(game_record, player, bank, bet)

        print("\t\tYour total is: %s\n" % self.total)

        hs = ''
        while hs.lower() != 'h' or hs.lower() != 's':
            hs = input("(h)HIT OR (s)STAND? ")
            if hs.lower() == 'h':
                return self.hit(game_record, dealer, player, bank, bet)
            elif hs.lower() == 's':
                print("\t\tSTAND")
                return dealer.reveal_hole_card(game_record, player, bank, bet)

    def hit(self, game_record, dealer, player, bank, bet):
        # choose random card from self.playing_cards
        x = random.randint(0, len(self.playing_cards) - 1)

        # append random card to hand
        self.hand.append(self.playing_cards[x])

        # store index of last card in hand and print it to screen for the player
        index_last_card = len(self.hand) - 1
        print("HIT: %s" % self.hand[index_last_card])

        # adding last hit to total
        card = self.hand[index_last_card]

        try:
            if card == 'A':
                # Check if +11 ace value is under 21, if not then +1 for ace value
                if self.total + 11 > 21:
                    self.total += 1
                    self.hand[index_last_card] = 1
                else:
                    self.total += 11
            # If card is Jack Queen or King. face card value is 10
            elif card in 'JQK':
                self.total += 10
        # If the card is a number it will output a TypeError for the elif above
        except TypeError:
            self.total += card

        # Checks for total and if player's first ace card must be changed to 1
        if self.total == 21:
            print("21! Nice Hit!\n")
            # Auto stand at 21. Dealer reveals their hole card
            return dealer.reveal_hole_card(game_record, player, bank, bet)
        # If total is over 21, check for any aces in hand and subtract 10 so A = 1 for the total
        elif self.total > 21 and 'A' in self.hand:
            self.total -= 10
            # Mutates list to avoid going over this elif
            self.hand[self.hand.index('A')] = 1
        elif self.total > 21:
            game_record[3] += 1
            game_record[1] += 1
            print("\t\tBUSTED")
            bank -= bet
            print("You lost $%.2f. Bank value is now: $%.2f" % (bet, bank))
            return bank

        print("Your total score is: %s\n" % self.total)
        hs = ''
        while hs.lower() != 'h' or hs.lower() != 's':
            hs = input("(h)HIT OR (s)STAND? ")
            if hs.lower() == 'h':
                return self.hit(game_record, dealer, player, bank, bet)
            elif hs.lower() == 's':
                print("\t\tSTAND")
                return dealer.reveal_hole_card(game_record, player, bank, bet)


# Inheritance from Player class

class Dealer(Player):

    def starting_hands(self):
        # prints first card in hand and second card is stored in hand variable
        for num in range(0, 2):
            x = random.randint(0, len(self.playing_cards) - 1)  # random integer from 0 - 12 (randint includes 12)
            self.hand.append(self.playing_cards[x])  # appends random card to hand variable

        return print("Dealer has %s and one hole card\n" % self.hand[0])

    def hit(self, game_record, player, bank, bet):
        # Cannot hit if already have BlackJack
        if self.total == 21:
            return

        # choose random card from self.playing_cards
        x = random.randint(0, len(self.playing_cards) - 1)

        # append random card to hand
        self.hand.append(self.playing_cards[x])

        # store index of last card in hand and print it to screen for the player
        index_last_card = len(self.hand) - 1
        print("Dealer hit: %s\n" % self.hand[index_last_card])

        # identifying card and adding last hit to total
        card = self.hand[index_last_card]

        try:
            if card == 'A':
                if self.total + 11 > 21:
                    self.total += 1
                    card = 1
                # Change ace value to +1 so total stays under 21
                else:
                    self.total += 11
            elif card in 'JQK':
                self.total += 10
        # If the card is a number it will output a TypeError for the elif above
        except TypeError:
            self.total += card

        # check for total is 21
        if self.total == 21:
            return print("\n\t\tDEALER HIT 21!\n")

        # If total is over 21, check for any aces in hand and subtract 10 so A = 1 for the total
        elif self.total > 21 and 'A' in self.hand:
            self.total -= 10
            self.hand[self.hand.index('A')] = 1

        print("Dealer total score is now: %s" % self.total)

    def reveal_hole_card(self, game_record, player, bank, bet):
        # hole card reveal and check for Dealer BlackJack
        print("\nDealer has %s and hole card is: %s" % (self.hand[0], self.hand[1]))

        # for each card in the hand, we add the equivalent value of the card
        for card in self.hand:
            try:
                if card == 'A':
                    if self.total + 11 > 21:
                        self.total += 1
                        self.hand[self.hand.index(card)] = 1
                    else:
                        self.total += 11
                elif card in 'JQK':
                    self.total += 10
            # If the card is a number it will output a TypeError for the elif above
            # Can check if card variable is a number rather than using 'try, except'
            except TypeError:
                self.total += card

        if self.total == 21:
            return print("Dealer has BlackJack!")
        else:
            print("Dealer total score is: %s\n" % self.total)
            # Dealer draws as long as their total is under 17
            while self.total < 17:
                print("Dealer takes a hit")
                self.hit(game_record, player, bank, bet)

                # game ends if dealer is closer to 21
                if 21 > self.total > player.total:
                    print("\n\t\tDEALER IS CLOSER TO 21, YOU LOSE!")
                    bank -= bet
                    print("You lost $%.2f. Bank value is now: $%.2f" % (bet, bank))
                    game_record[1] += 1
                    return bank

            if self.total > 21:
                game_record[0] += 1
                print("\t\tYOU WIN!")
                bank += bet
                print("You gained %.2f. Bank value is now: $%.2f" % (bet, bank))
                return bank
            elif player.total > self.total:
                print("\n\t\tPLAYER IS CLOSER TO 21, YOU WIN!")
                bank += bet
                print("You gained $%.2f. Bank value is now: $%.2f" % (bet, bank))
                game_record[0] += 1
                return bank
            elif self.total > player.total:
                print("\n\t\tYOU LOSE!")
                bank -= bet
                print("You lost $%.2f. Bank value is now: $%.2f" % (bet, bank))
                game_record[1] += 1
                return bank
            else:
                print("ITS A DRAW!")
                bank -= bet
                print("The house always wins.\nYou lose $%.2f\nBank Value is now: %.2f" % (bet, bank))
                game_record[3] += 1
                return bank
