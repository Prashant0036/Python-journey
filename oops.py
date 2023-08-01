
class College:
    pass


class Student (College):
    roll1=1
    marks=20
    def __init__(self) -> None:
        print("This is Constructor stu")


   # @staticmethod
    def method1(self):
        print(" This is Method 1 of class Student")
    
    
class Boys(Student):
    def __init__(self) -> None:
        super().__init__()              
        print("This is boy class Costr.")
    #method1()

Student.marks=40
st=Student()
st.marks=40
st1=Student()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
print(st1.marks)
boy=Boys()
boy.method1()
st.roll1=2
print(st.marks)
print(st1.roll1)