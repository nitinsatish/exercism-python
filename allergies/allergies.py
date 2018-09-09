class Allergies(object):


    def __init__(self, score):
        value_item = { 
            'egg': 1, 
            'peanut' : 2,
            'shellfish' : 4,
            'strawberries' : 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats' :128,
            }

        

    def is_allergic_to(self, item):
        if score % 256 == 0 :
            return False
        elif value_item[item] == score :
            return True
        
        
        




    @property
    def lst(self):
        pass
