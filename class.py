import pandas as pd
from student import Student


class Class():
    def __init__(self, students: list[Student]):
        self.students = students
        ...
    
    # load name_list, create class object
    @classmethod
    def loadFromCsv(cls, class_name): # class_name = name of the classroom
        file_name = f'{class_name}.csv'
        df = pd.read_csv(file_name)
        student_list = []
        # TODO:
        for row in df.itertuples():
            student_list.append(Student(row.first_name, row.last_name, row.country))
        # TODO: 
        # create a class obj 
        return cls(student_list)       
    
    def getStudentCount(self):
        ...

def main():
    # load 'class 101' student's csv
    class_list = Class.loadFromCsv('101')
    print('content')
    print(class_list.students[0].print_info())
    print('end')
    
    
        
if __name__ == "__main__":
    main()