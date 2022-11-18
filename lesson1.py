# полиморфизм
# from random import randint
#
#
# class Triangle:
#     def __init__(self, count):
#         self.names_value = {f"side_{i}": randint(1, 20) for i in range(count)}
#         self.square = 0
#
#     def get_attrs(self):
#         print(list(self.__dict__.items()))
#
#     def distract_square(self):
#         square = 1 / 2 * self.names_value["side_0"] * self.names_value["side_1"]
#         self.square = square
#         print(self.square)
#
# trinagle1 = Triangle(2)
# trinagle2 = Triangle(2)
# trinagle1.distract_square()
# trinagle2.distract_square()
# trinagle1.get_attrs()
# trinagle2.get_attrs()



# class Student:
#     def __init__(self, full_name, course: int):
#         self.full_name = full_name
#         self.course = course
#         # self.subjects = subjects
#         # self.total = 0
#
#     def set_subjects(self, subjects: dict) -> None :
#         self.subjects = subjects
#
#     def total(self):
#         self.average = sum(self.subjects.values()) / len(self.subjects)
#
#     def save_total(self):
#         with open(f'{self.full_name}.txt', 'a') as f:
#             f.write(f'{self.full_name} - {self.course} - {self.total()}\n')
#
#
#     def set_course(self):
#         self.course += 1
#
#
#
# qwert1 = Student(full_name='Aasd', course=3)
# subjects = {
#     "python": 56,
#     "math": 99
# }
# qwert1.set_subjects(subjects)
# qwert1.save_total()
