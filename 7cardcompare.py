from functools import cmp_to_key
import sys

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return str(self.rank)+ " " +str(self.suit) + "\n"
    def equal(card1, card2):
        return self.rank == othercard.rank and self.suit == othercard.suit
def cardCompare(card1, card2):
    if(card1.rank > card2.rank):
        return -1
    elif(card1.rank == card2.rank):
        return 0
    else:
        return 1
class SevenCardHand:
    def __init__(self, cardArray):
        self.cardArray = sorted(cardArray, key=cmp_to_key(cardCompare))
        self.rank = -1
    def __str__(self):
        blank = ""
        for i in range(len(self.cardArray)):
            blank = blank + str(self.cardArray[i])
        return blank
    def hasPair(self):
        #assumes no higher hand also assumes cardArray is sorted
        for i in range(len(self.cardArray) - 1):
            if (self.cardArray[i].rank == self.cardArray[i + 1].rank):
                    return (True, self.cardArray[i].rank)
        return (False, -1)
    def has2Pair(self):
        cardArray = self.cardArray.copy()
        #assumes no higher hands also assumes cardArray is sorted
        temp = SevenCardHand(cardArray)
        if (temp.hasPair()[0]):
            rankPair1 = self.hasPair()[1]
            listcount = 0
            while (listcount < len(cardArray)):
                if cardArray[listcount].rank == rankPair1:
                    cardArray.remove(cardArray[listcount])
                    listcount = listcount - 1
                listcount = listcount + 1

            temp = SevenCardHand(cardArray)

            if (temp.hasPair()[0]):
                rankPair2 = temp.hasPair()[1]

                listcount = 0
                while (listcount < len(cardArray)):
                    if cardArray[listcount].rank == rankPair2:
                        cardArray.remove(cardArray[listcount])
                        listcount = listcount - 1
                    listcount = listcount + 1

                return (True, rankPair1, rankPair2, cardArray[0].rank)

        return (False, -1, -1, -1)
    def hasTriple(self):
        for i in range(len(self.cardArray) - 2):
            if (self.cardArray[i].rank == self.cardArray[i + 1].rank and self.cardArray[i + 1].rank ==
                self.cardArray[i + 2].rank):
                return (True, self.cardArray[i].rank)
        return (False, -1)
    def hasStraight(self):

        for i in range(len(self.cardArray)-5):
            if (self.cardArray[i + 1].rank == self.cardArray[i].rank - 1 and
                self.cardArray[i + 2].rank == self.cardArray[i].rank - 2 and
                self.cardArray[i + 3].rank == self.cardArray[i].rank - 3 and
                self.cardArray[i + 4].rank == self.cardArray[i].rank - 4):
                return (True, self.cardArray[i].rank)

        checker = []
        for i in range(len(self.cardArray)):
            if (self.cardArray[i].rank == 14):
                checker.append(0)
            if (self.cardArray[i].rank == 2):
                checker.append(0)
            if (self.cardArray[i].rank == 3):
                checker.append(0)
            if (self.cardArray[i].rank == 4):
                checker.append(0)
            if (self.cardArray[i].rank == 5 ):
                checker.append(0)
        if len(checker) == 5:
            return True, 5
        return (False, -1)
    def hasFlush(self):
        count = 0
        highestnumber = -1
        for i in range(len(self.cardArray)):
            if (self.cardArray[i].suit == 1):
                count += 1
                if (highestnumber == -1):
                    highestnumber = self.cardArray[i].rank
        if (count >= 5):
            return (True, 1, highestnumber)

        count = 0
        highestnumber = -1
        for i in range(len(self.cardArray)):
            if (self.cardArray[i].suit == 2):
                count += 1
                if (highestnumber == -1):
                    highestnumber = self.cardArray[i].rank
        if (count >= 5):
            return (True, 2, highestnumber)

        count = 0
        highestnumber = -1
        for i in range(len(self.cardArray)):
            if (self.cardArray[i].suit == 3):
                count += 1
                if (highestnumber == -1):
                    highestnumber = self.cardArray[i].rank
        if (count >= 5):
            return (True, 3, highestnumber)

        count = 0
        highestnumber = -1
        for i in range(len(self.cardArray)):
            if (self.cardArray[i].suit == 4):
                count += 1
                if (highestnumber == -1):
                    highestnumber = self.cardArray[i].rank
        if (count >= 5):
            return (True, 4, highestnumber)
        return (False, -1, -1)
    def hasFullHouse(self):
        cardArray = self.cardArray.copy()
        temp = SevenCardHand(cardArray)
        if (temp.hasTriple()[0]):
            rankTriple1 = temp.hasTriple()[1]
            listcount = 0
            while (listcount < len(cardArray)):
                if (cardArray[listcount].rank == rankTriple1):
                    cardArray.remove(cardArray[listcount])
                    listcount = listcount - 1
                listcount = listcount + 1
            temp = SevenCardHand(cardArray)
            if temp.hasPair()[0]:
                return True, rankTriple1, temp.hasPair()[1]
        return False, -1, -1
    def hasQuads(self):
        for i in range(len(self.cardArray) - 3):
            if (self.cardArray[i].rank == self.cardArray[i + 1].rank and
                self.cardArray[i + 1].rank == self.cardArray[i + 2].rank and
                self.cardArray[i + 2].rank == self.cardArray[i + 3].rank):
                return (True, self.cardArray[i].rank)
        return (False, -1)
    def hasStraightFlush(self):

        for i in range(len(self.cardArray)-4):
            if (self.cardArray[i + 1].rank == self.cardArray[i].rank - 1 and
                self.cardArray[i + 2].rank == self.cardArray[i].rank - 2 and
                self.cardArray[i + 3].rank == self.cardArray[i].rank - 3 and
                self.cardArray[i + 4].rank == self.cardArray[i].rank - 4 and
                self.cardArray[i + 1].suit == self.cardArray[i].suit and
                self.cardArray[i + 2].suit == self.cardArray[i].suit and
                self.cardArray[i + 3].suit == self.cardArray[i].suit and
                self.cardArray[i + 4].suit == self.cardArray[i].suit):
                return (True, self.cardArray[i].rank, self.cardArray[i].suit)

        checker = []
        for i in range(len(self.cardArray)):
            if (self.cardArray[i].rank == 14):
                checker.append(self.cardArray[i].suit)
            if (self.cardArray[i].rank == 2):
                checker.append(self.cardArray[i].suit)
            if (self.cardArray[i].rank == 3):
                checker.append(self.cardArray[i].suit)
            if (self.cardArray[i].rank == 4):
                checker.append(self.cardArray[i].suit)
            if (self.cardArray[i].rank == 5):
                checker.append(self.cardArray[i].suit)
        if len(checker) == 5:
            suit = checker[0]
            booleanchecker = True
            for i in checker:
                if not i == suit:
                    booleanchecker = False
            if booleanchecker:
                return True, 5, suit
        return False, -1, -1
    def ranks(self):

        if (self.hasStraightFlush()[0]):
            self.rank = 8
        elif (self.hasQuads()[0]):
            self.rank = 7
        elif (self.hasFullHouse()[0]):
            self.rank = 6
        elif (self.hasFlush()[0]):
            self.rank = 5
        elif (self.hasStraight()[0]):
            self.rank = 4
        elif (self.hasTriple()[0]):
            self.rank = 3
        elif (self.has2Pair()[0]):
            self.rank = 2
        elif (self.hasPair()[0]):
            self.rank = 1
        else:
            self.rank = 0


    def test(self):
        print("Pair")
        print(self.hasPair())
        print("2Pair")
        print(self.has2Pair())
        print("Trips")
        print(self.hasTriple())
        print("Straight")
        print(self.hasStraight())
        print("Flush")
        print(self.hasFlush())
        print("FullHouse")
        print(self.hasFullHouse())
        print("Quads")
        print(self.hasQuads())
        print("Straight Flush")
        print(self.hasStraightFlush())

def sevenCardHandCompare(hand1, hand2):
    if(hand1.rank > hand2.rank):
        return 1
    elif(hand1.rank < hand2.rank):
        return -1
    else:
        #inferred that hand1.rank == hand2.rank
        if(hand1.rank == 8):
            return hand1.hasStraightFlush()[1] - hand2.hasStraightFlush()[1]
        elif(hand1.rank == 7):
            if(hand1.hasQuads()[1] - hand2.hasQuads()[1] == 0):
                hand1notQuad = -1
                hand2notQuad = -1
                for i in range(7):
                    if not hand1[i].rank == hand1.hasQuads() and hand1notQuad == -1:
                        hand1notQuad = hand1[i].rank
                for i in range(7):
                    if not hand2[i].rank == hand2.hasQuads() and hand2notQuad == -1:
                        hand2notQuad = hand2[i].rank
                return hand1notQuad - hand2notQuad
            return hand1.hasQuads()[1] - hand2.hasQuads()[1]

        elif(hand1.rank == 6):
            if(hand1.hasFullHouse()[1] - hand2.hasFullHouse()[1] == 0):
                return hand1.hasFullHouse()[2] - hand2.hasFullHouse()[2]
            return hand1.hasFullHouse()[1] - hand2.hasFullHouse()[1]
        elif(hand1.rank == 5):
            count = 0
            suit1 = hand1.hasFlush()[1]
            flushArray1 = []
            for i in range(7):#all hands have 7 cards
                if (count < 5 and hand1.cardArray[i].suit == suit1):
                    flushArray1.append(hand1.cardArray[i].rank)
            count = 0
            suit2 = hand2.hasFlush()[1]
            flushArray2 = []
            for i in range(7):
                if (count < 5 and hand2.cardArray[i].suit == suit2):
                    flushArray2.append(hand1.cardArray[i].rank)
            for i in range(len(flushArray1)): #flushArray1 and flushArray2 both have 5 cards
                if flushArray1[i] > flushArray2[i]:
                    return 1
                elif flushArray1[i] < flushArray2[i]:
                    return -1
            return 0
        elif(hand1.rank == 4):
            return hand1.hasStraight()[1] - hand2.hasStraight()[1]
        elif(hand1.rank == 3):
            if(hand1.hasTriple()[1] - hand2.hasTriple()[1] == 0):
                hand1notTrip = []
                hand2notTrip = []
                for i in range(7):
                    if not hand1[i].rank == hand1.hasTriple() and len(hand1notTrip) < 3:
                        hand1notTrip.append(hand1[i].rank)
                for i in range(7):
                    if not hand2[i].rank == hand2.hasTriple() and len(hand2notTrip) < 3:
                        hand2notTrip.append(hand2[i].rank)
                if (hand1notTrip[0] - hand2notTrip[0] == 0):
                    return hand1notTrip[1] - hand2notTrip[1]
                return hand1notTrip[0] - hand2notTrip[0]

            return hand1.hasTriple()[1] - hand2.hasTriple()[1]
        elif(hand1.rank == 2):
            twoPair1 = hand1.has2Pair()
            twoPair2 = hand2.has2Pair()
            if(twoPair1[1] - twoPair2[1] == 0):
                if(twoPair1[2] - twoPair2[2] == 0):
                    return twoPair1[3] - twoPair2[3]
                return twoPair1[2] - twoPair2[2]
            return twoPair1[1] - twoPair2[1]
        elif(hand1.rank == 1):
            if(hand1.hasPair()[1] - hand2.hasPair()[1] == 0):
                hand1notPair = []
                hand2notPair = []
                for i in range(7):
                    if not hand1[i].rank == hand1.hasPair() and len(hand1notPair) < 4:
                        hand1notPair.append(hand1[i].rank)
                for i in range(7):
                    if not hand2[i].rank == hand2.hasPair() and len(hand2notPair) < 4:
                        hand2notPair.append(hand2[i].rank)

                if (hand1notPair[0] - hand2notPair[0] == 0):
                    if (hand1notPair[1] - hand2notPair[1] == 0):
                        return hand1notPair[2] - hand2notPair[2]
                    return hand1notPair[1] - hand2notPair[1]
                return hand1notPair[0] - hand2notPair[0]

            return hand1.hasPair()[1] - hand2.hasPair()[1]

        else:
            if(hand1.cardArray[0] - hand2.cardArray[0] == 0):
                if(hand1.cardArray[1] - hand2.cardArray[1] == 0):
                    if(hand1.cardArray[2] - hand2.cardArray[2] == 0):
                        if(hand1.cardArray[3] - hand2.cardArray[3] == 0):
                            return hand1.cardArray[4] - hand2.cardArray[4]
                        return hand1.cardArray[3] - hand2.cardArray[3]
                    return hand1.cardArray[2] - hand2.cardArray[2]
                return hand1.cardArray[0] - hand2.cardArray[0]
            return hand1.cardArray[0] - hand2.cardArray[0]





def testKingsFullofAces():
    card1 = Card(14, 3)
    card2 = Card(14, 4)
    card3 = Card(13, 2)
    card4 = Card(13, 3)
    card5 = Card(13, 1)
    card6 = Card(9, 3)
    card7 = Card(7, 3)
    #card2 = Card(14, 4)
    cardArray = []
    cardArray.append(card1)
    cardArray.append(card2)
    cardArray.append(card3)
    cardArray.append(card4)
    cardArray.append(card5)
    cardArray.append(card6)
    cardArray.append(card7)

    aceHighFlush = SevenCardHand(cardArray)
    aceHighFlush.ranks()
    print(aceHighFlush.rank)
    #aceHighFlush.test()
    print("\n")

def testQuad2s():
    card1 = Card(2, 1)
    card2 = Card(2, 2)
    card3 = Card(2, 3)
    card4 = Card(2, 4)
    card5 = Card(13, 1)
    card6 = Card(9, 3)
    card7 = Card(7, 3)
    #card2 = Card(14, 4)
    cardArray = []
    cardArray.append(card1)
    cardArray.append(card2)
    cardArray.append(card3)
    cardArray.append(card4)
    cardArray.append(card5)
    cardArray.append(card6)
    cardArray.append(card7)

    quad2 = SevenCardHand(cardArray)
    quad2.ranks()
    print(quad2.rank)
    #quad2.test()
    print("\n")

def testStraightFlush():
    card1 = Card(2, 1)
    card2 = Card(3, 1)
    card3 = Card(4, 1)
    card4 = Card(5, 1)
    card5 = Card(14, 1)
    card6 = Card(9, 3)
    card7 = Card(7, 3)
    #card2 = Card(14, 4)
    cardArray = []
    cardArray.append(card1)
    cardArray.append(card2)
    cardArray.append(card3)
    cardArray.append(card4)
    cardArray.append(card5)
    cardArray.append(card6)
    cardArray.append(card7)

    straightflush = SevenCardHand(cardArray)
    straightflush.ranks()
    print(straightflush.rank)
    #straightflush.test()

def testQuadsvsQuads():
    card1 = Card(2, 1)
    card2 = Card(2, 2)
    card3 = Card(2, 3)
    card4 = Card(2, 4)
    card5 = Card(13, 1)
    card6 = Card(9, 3)
    card7 = Card(7, 3)
    cardArray = []
    cardArray.append(card1)
    cardArray.append(card2)
    cardArray.append(card3)
    cardArray.append(card4)
    cardArray.append(card5)
    cardArray.append(card6)
    cardArray.append(card7)
    quad2 = SevenCardHand(cardArray)
    quad2.ranks()
    print(quad2.rank)
    print("\n")

    card1 = Card(3, 1)
    card2 = Card(3, 2)
    card3 = Card(3, 3)
    card4 = Card(3, 4)
    card5 = Card(13, 1)
    card6 = Card(9, 3)
    card7 = Card(7, 3)
    cardArray = []
    cardArray.append(card1)
    cardArray.append(card2)
    cardArray.append(card3)
    cardArray.append(card4)
    cardArray.append(card5)
    cardArray.append(card6)
    cardArray.append(card7)
    quad1 = SevenCardHand(cardArray)
    quad1.ranks()
    print(quad1.rank)
    print(sevenCardHandCompare(quad2, quad1))
    print("\n")

def testFlushoverFlush():
    card1 = Card(2, 1)
    card2 = Card(3, 1)
    card3 = Card(5, 1)
    card4 = Card(6, 1)
    card5 = Card(13, 1)
    card6 = Card(9, 3)
    card7 = Card(7, 3)
    cardArray = []
    cardArray.append(card1)
    cardArray.append(card2)
    cardArray.append(card3)
    cardArray.append(card4)
    cardArray.append(card5)
    cardArray.append(card6)
    cardArray.append(card7)
    flush1 = SevenCardHand(cardArray)
    flush1.ranks()
    print(flush1.rank)
    print("\n")

    card1 = Card(14, 1)
    card2 = Card(2, 1)
    card3 = Card(3, 3)
    card4 = Card(8, 1)
    card5 = Card(13, 1)
    card6 = Card(9, 1)
    card7 = Card(7, 3)
    cardArray = []
    cardArray.append(card1)
    cardArray.append(card2)
    cardArray.append(card3)
    cardArray.append(card4)
    cardArray.append(card5)
    cardArray.append(card6)
    cardArray.append(card7)
    flush2 = SevenCardHand(cardArray)
    flush2.ranks()
    print(flush2.rank)
    print(sevenCardHandCompare(flush1, flush2))
    print("\n")

def main():
    #testKingsFullofAces()
    #testQuad2s()
    #testStraightFlush()
    testQuadsvsQuads()
    testFlushoverFlush()
if __name__ == "__main__":
    main()
