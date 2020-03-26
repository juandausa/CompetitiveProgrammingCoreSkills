class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


    def __eq__(self, other):
        return self.get_performace() == other.get_performace()


    def __lt__(self, other):
        return self.get_performace() < other.get_performace()


    def get_performace(self):
        return self.value/self.weight
