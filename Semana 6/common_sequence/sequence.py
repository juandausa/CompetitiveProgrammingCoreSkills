class Sequence(object):
    def __init__(self, values = None):
        self.values = values if values is not None else []
    
    
    def len(self):
        return len(self.values)
    
    def __add__(self, other): 
        self.values += other.values
        return self


    def __eq__(self, other):
        return self.len() == other.len()


    def __lt__(self, other):
        return self.len() < other.len()