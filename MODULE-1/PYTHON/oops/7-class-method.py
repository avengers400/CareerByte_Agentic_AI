class Student:
    school = "Delhi Public School"

    @classmethod
    def display(cls):
        print(cls.school)

Student.display()