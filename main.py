from class import Class
from student import Student

stu = Student("peter", 'law' , "HK")
stu.print_info()
stu.doTest()
stu.printScore()
class101 = Class.loadFromCsv('101')
class101.getStudentCount()
class101.getStudentList()
class101.toTest()
class101.getAverageScore('kanji')


### why I just hate naming file in CN, JP now.
### https://learn.microsoft.com/zh-cn/answers/questions/3155934/0x800700ea