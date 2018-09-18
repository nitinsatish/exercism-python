value_item = { 
    'eggs': 1, 
    'peanuts' : 2,
    'shellfish' : 4,
    'strawberries' : 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats' :128,
    }
        
class Allergies(object):


    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        item_score = value_item[item]
        return item_score & self.score == item_score


    @property
    def lst(self):
        allergies = []
        for k in value_item.keys() :
            if self.is_allergic_to(k) :
                allergies.append(k)
        return allergies



