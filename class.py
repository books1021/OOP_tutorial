import pandas as pd
from student import Student
import random

class Class():
    def __init__(self, student_list : list[Student]): 
        self.students = student_list

        ...
    
    # load name_list, create class object
    @classmethod
    def loadFromCsv(cls, class_name): # class_name = name of the classroom
        file_name = f'{class_name}.csv'
        df = pd.read_csv(file_name)
        student_list = []
        for row in df.itertuples():
            student_list.append(Student(row.first_name, row.last_name, row.country))
        # create a class obj 
        return cls(student_list)       
    
    def getStudentCount(self):
        return(len(self.students))

    def getStudentList(self):
        name_list = []
        for student in self.students:
             name_list.append(f'{student.first_name} {student.last_name}')
        return name_list
            
    def toTest(self):
        for student in self.students:
            student.doTest()
            ...
            
    def getAverageScore(self, sub : str):
        # TODO optimize this
        if sub not in ('kanji','bunpou','katakana'):
            # create error warning
            print('wrong subject name')
        if sub in ('kanji','bunpou','katakana'):
            sum = 0
            for student in self.students:
                sum = sum + getattr(student,sub)
            average = sum / len(self.students)
            return average
        
    def seatSuffle(self):
        # TODO seat suffle
        # generate a permuatation sequence
        # seat_permutation = random.shuffle(list(range(1, len(self.students))))
        # [self.students, seat_permutation]
        random.shuffle(self.students)
        for seat, student in enumerate(self.students, start = 1):
            student.seat_number = seat
        ...
    

                
            


### why so slow???
def main():
    # load 'class 101' student's csv
    class_list = Class.loadFromCsv('101')
    print('student count')
    # class_list.students[0].print_info()
    class_list.getStudentCount()
    print('all names')
    class_list.getStudentList()
    print('do test')
    class_list.toTest()
    class_list.students[0].printScore()
    print('end')
    
    
        
if __name__ == "__main__":
    main()