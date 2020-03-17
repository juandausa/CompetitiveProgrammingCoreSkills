from rank import Rank


def straight_flush(cards):
    suits = map(getSuit, cards)
    if(len(set(suits)) != 1):
        return False

    if (not cardsInOrder(map(getRank, cards))):
        return False

    return True


def getSuit(card):
    return card[-1:]


def getRank(card):
    return card[:-1]


def cardsInOrder(ranks):
    sortedRanks = list(map(createRank, ranks))
    sortedRanks.sort()
    asRank = Rank('A')
    if (asRank in sortedRanks):
        sortedRanks.pop(0)
        for rank in sortedRanks:
            if (rank == sortedRanks[len(sortedRanks)-1]):
                continue
            if(rank.getNextValue() not in sortedRanks):
                return False
        return (Rank('2') in sortedRanks or Rank('K') in sortedRanks)
    else:
        for rank in sortedRanks:
            if (rank == sortedRanks[len(sortedRanks)-1]):
                continue
            if(rank.getNextValue() not in sortedRanks):
                return False

    return True


def createRank(rank):
    return Rank(rank)
