# heirarchical inheritance
# single parent multiple child

class College:
  college_name = ""
  college_location = ""

  def running(self):
    print("College is Running")

class Student(College):
  student_name = ""
  roll_no = 0
  marks = 0

  def display(self):
    print("College Name:",self.college_name)
    print("College Location:",self.college_location)
    print("Student Name:",self.student_name)
    print("Roll No:",self.roll_no)
    print("Marks:",self.marks)

class Teacher(College):
  teacher_name = ""
  subject = ""

  def display(self):
    print("College Name:",self.college_name)
    print("College Location:",self.college_location)
    print("Teacher Name:",self.teacher_name)
    print("Subject:",self.subject)

s = Student()
s.college_name = "ABC College"
s.college_location = "Pune"
s.student_name = "John"
s.roll_no = 101
s.marks = 90
s.display()

print("--------------------------------")

t = Teacher()
t.college_name = "ABC College"
t.college_location = "Pune"
t.teacher_name = "Mary"
t.subject = "Maths"
t.display()
