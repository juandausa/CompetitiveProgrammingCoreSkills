class Rank:
    order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    def __init__(self, rank):
        self.rank = rank
    
    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return (Rank.order.index(self.rank) < Rank.order.index(other.rank))

    def getNextValue(self):
        try:
            decimalRank = int(self.rank)
            if (decimalRank <= 9):
                return Rank(str(decimalRank+1))
            else:
                return Rank("J")
        except ValueError:
            if (self.rank == "J"):
                return Rank("Q")
            elif (self.rank == "Q"):
                return Rank("K")
            elif (self.rank == "K"):
                return Rank("A")
            elif(self.rank == "A"):
                return Rank("2")