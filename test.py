from sevencardcompare import Card
from sevencardcompare import SevenCardHand
from sevencardcompare import sevenCardHandCompare
import random

def buildBoard(deck):#deck is a list of cards
    indexes = []
    while len(indexes) < 5:
        randomcardindex = random.randrange(0,len(deck))
        if not(randomcardindex in indexes):
            indexes.append(randomcardindex) #type of indexes
        actualboard = []

    for i in indexes:
        actualboard.append(deck[i])
    return actualboard #at the end of this, actualboard is length 5, and has the corresponding cards to the randomly generated indexes in indexes.

player1cardranks = [14,14]
player1cardsuits = [4,3]
player2cardranks = [11,11]
player2cardsuits = [4,3]
player1 = [Card(player1cardranks[0], player1cardsuits[0]), Card(player1cardranks[1],player1cardsuits[1])]
player2 = [Card(player2cardranks[0], player2cardsuits[0]), Card(player2cardranks[1],player2cardsuits[1])]

deck = [] #building a deck of 52 cards
for i in range(2,15):
    for j in range(1,5):
        if not(i == player1cardranks[0] and j==player1cardsuits[0]) and not(i == player1cardranks[1] and j==player1cardsuits[1]) and not(i == player2cardranks[0] and j==player2cardsuits[0]) and not(i == player2cardranks[1] and j==player1cardsuits[1]):
            deck.append(Card(i,j))


# deck = list(set(deck) - set(player1)) #subtract player 1 and player2 cards from the deck so you have no repeats on board.
# deck = list(set(deck) - set(player2))
# for i in deck:
#     print(i)


n = 10000
player1wins = 0
player2wins = 0
for i in range(n):

    board = buildBoard(deck)
    # total = "["
    # for i in board:
    #     total = total +  str(i) + ","
    # print (total + "]")

    player1cardArray = player1 + board
    player2cardArray = player2 + board

    player1_7cardHand = SevenCardHand(player1cardArray)
    player2_7cardHand = SevenCardHand(player2cardArray)

    # print("player1's seven card hand" + str(player1_7cardHand))
    # print("player2's seven card hand" + str(player2_7cardHand))

    player1_7cardHand.ranks()
    player2_7cardHand.ranks()
    result = sevenCardHandCompare(player1_7cardHand, player2_7cardHand)
    #print(result)
    #print(type(player2_7cardHand))

    if result > 0:
        player1wins = player1wins + 1
    elif result < 0:
        player2wins = player2wins + 1
    else:
        player2wins = player2wins + 0.5
        player1wins = player1wins + 0.5

print("final score!")
print(player1wins/(player1wins + player2wins))
