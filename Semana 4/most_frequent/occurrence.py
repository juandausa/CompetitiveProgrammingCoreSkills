from collections import Counter
import operator


class Occurrence:
    def __init__(self, character=None, occurrence=None):
        if (not character is None):
            self.occurrences = dict({character: occurrence})
        else:
            self.occurrences = dict()

    def add(self, other_occurrence):
        self.occurrences = dict(
            Counter(self.occurrences) + Counter(other_occurrence.occurrences))

    def get_occurrence(self, character):
        return self.occurrences[character] if character in self.occurrences.keys() else 0

    def get_element_with_maximum_occurrence(self):
        assert len(self.occurrences) > 0
        return max(self.occurrences.items(), key=operator.itemgetter(1))[0]
