import random

class Student():
    def __init__(self, first_name, last_name, country, kanji : (int,float) = None, bunpou : (int,float) = None, katakana : (int,float) = None, seat_number = None):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.kanji = kanji
        self.bunpou = bunpou
        self.katakana = katakana
        self.passion = random.randint(1,10) 
        self.seat_number = seat_number

    
    def print_info(self):
        print(f'{self.first_name} {self.last_name} {self.country}')
    
    # randomly generate scores
    # assume 0 <= score <= 100
    def doTest(self):
        #TODO
        ### request explaination on modify doTest
        ### build a better structure
        if self.country not in {'Taiwan','HongKong','China','Singapore','Malaysia','Korean'}:
            self.kanji = random.randint(self.passion, 15)*6 + random.randint(0,10)
        if self.country in {'Taiwan','HongKong'}:
            self.kanji = random.randint(self.passion + 3, 15)*6 + random.randint(0,10)
        if self.country in {'China','Singapore','Malaysia'}:
            self.kanji = random.randint(self.passion + 2, 15)*6 + random.randint(0,10)                        
        # bunpou part 
        if self.country =! 'Korea':
            self.bunpou = random.randint(self.passion, 15)*6 + random.randint(0,10)
        if self.country = 'Korea':
            self.bunpou = random.randint(self.passion + 2, 15)*6 + random.randint(0,10)
        # katakana    
        self.katakana = random.randint(self.passion, 15)*6 + random.randint(0,10)
    
    def printScore(self):
        print({'kanji' : self.kanji, 'bunpou' : self.bunpou, 'katakana' : self.katakana}) 

