import random
import statistics

WIN_TAKE = 1.5  # Win: Get 50% more
LOSE_TAKE = .6  # Lose: Lose 40%

NUMBER_OF_COIN_FLIPS = 1000

# An ensemble is a series of coin flips. Any single ensemble is you.
NUMBER_OR_ENSEMBLES = 1000

# The BET_PERCENT is percent of your money you put into each bet
# Try changing this to .25 to see what will happen when you do 4 bets at 25% instead of always doing 1 bet of 100%!
BET_PERCENT = 1

# The claim is that the average amount of money won across all ensembles will go up, but for any 1 ensemble over a long period of
# time, half the time they will lose money.
INITIAL_AMOUNT = 100
MAX_BET = 100

ENSEMBLES = []

global WINNING_ENSEMBLES
WINNING_ENSEMBLES = 0


'''
ENSEMBLES should be an array of arrays. Each ensemble is a person but a person can have multiple bets.
For example, if there were 2 ensembles and each ensemble had 4 bets of 25%, initial ENSEMBLES value would look like:
[[25,25,25,25],[25,25,25,25]]
Each person, AKA "ensemble", will get to play 4 games.
'''
def initialize_ensembles(bet_percent=1):
    for ensemble in range(NUMBER_OR_ENSEMBLES):
        num_bets = int(INITIAL_AMOUNT // (INITIAL_AMOUNT * bet_percent))
        ENSEMBLES.append(
            [INITIAL_AMOUNT * bet_percent for x in range(num_bets)])


def flip_coin(bet):
    # 50/50 chance
    if random.randrange(2):
        return bet * WIN_TAKE
    else:
        return bet * LOSE_TAKE


def play_game(balance):
    for x in range(NUMBER_OF_COIN_FLIPS):
        ''' 
        If a person has more than the MAX_BET, they can't bet their entire balance.
        '''
        if balance > MAX_BET:
            winnings = flip_coin(MAX_BET)
            balance = (balance-MAX_BET) + winnings
        else:
            winnings = flip_coin(balance)
            balance = winnings
    return balance


def get_average_won():
    return statistics.mean((sum(e) for e in ENSEMBLES))


def get_median_won():
    return statistics.median([sum(e) for e in ENSEMBLES])


def get_total_won():
    return sum([sum(e) for e in ENSEMBLES])


def get_max_won():
    return max([sum(e) for e in ENSEMBLES])


def format_money(amount):
    return "${:,.2f}".format(amount)


def print_results():
    print("Number OF ENSEMBLES: " + str(NUMBER_OR_ENSEMBLES))
    print("Number OF Coin Flips: " + str(NUMBER_OF_COIN_FLIPS))
    print("Total Money in System: " + str(format_money(get_total_won())))
    print("Max Final Balance: " + str(format_money(get_max_won())))
    print("Average Final Balance: " + str(format_money(get_average_won())))
    print("Median Final Balance: " + str(format_money(get_median_won())))
    print("Number of Ensembles with less than $100: " +
          str(NUMBER_OR_ENSEMBLES-WINNING_ENSEMBLES))
    print("Number of Ensembles with more than $100: " +
          str(WINNING_ENSEMBLES))


initialize_ensembles(bet_percent=BET_PERCENT)
for x in range(len(ENSEMBLES)):
    ensemble = ENSEMBLES[x]
    for x in range(len(ensemble)):
        balance = ensemble[x]
        ensemble[x] = play_game(balance)
    if sum(ensemble) > 100:
        WINNING_ENSEMBLES += 1
print_results()
