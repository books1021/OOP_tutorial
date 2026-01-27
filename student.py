import random

class Student():
    def __init__(self, first_name, last_name, country, kanji : (int,float) =None, bunpou : (int,float) =None, katakana : (int,float) =None):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.kanji = kanji
        self.bunpou = bunpou
        self.katakana = katakana
    
    def print_info(self):
        print(f'{self.first_name} {self.last_name} {self.country}')
    
    # randomly generate scores
    # assume 0 <= score <= 100
    def doTest(self):
        self.kanji = random.randint(0, 100)
        self.bunpou = random.randint(0, 100)
        self.katakana = random.randint(0, 100)
    
    def printScore(self):
        print({'kanji' : self.kanji, 'bunpou' : self.bunpou, 'katakana' : self.katakana}) 