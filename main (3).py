
class Student:
  def __init__(self,name,roll_number,cgpa):
    self . name =name
    self . roll_number =roll_number
    self . cgpa =cgpa
def sort_students(student_list):
  Sorted_students = sorted(student_list,key=lambda student : student.cgpa,reverse=True)
  return Sorted_students

#example usage:
Students=[Student("Yashika","A123",7.8),
         Student("Yas","A124",8.9),
         Student("Raj","A125",9.1),
         Student("Ramanan","A126",9.9)]
Sorted_students=sort_students(Students)
for student in Sorted_students:
  print("Name: {},Roll Number: {},CGPA: {}".format(student.name,student.roll_number,student.cgpa))
  
  

