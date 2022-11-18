# mro - порядок разрешений методов
# staticmethod, classmethod, isinstance method

# from datetime import datetime
# class Person:
#     spec  = "Programmist"
#     it_major = ["pm", "devops", "tester", "developer", "analytyc", "ux-ui"]
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def create_object(cls, name, year):
#         now_date = datetime.now().year
#         age = now_date - year
#         return cls(name, age)
#
#     @classmethod
#     def create_object_with_cls(cls, new_spec):
#         print(new_spec.name)
#         # if new_spec.lower() in cls.it_major:
#         #     cls.spec = new_spec
#
#     def get_person(self):
#         print("{name} {age}".format(name=self.name, age=self.age))
#
#
# arsen = Person("Ars", 17)
# aabesov = Person.create_object("Arsen", 2005)
# aabesov.get_person()


#
#
# from datetime import datetime
# my_dict = {
#     "name": "Alex",
#     "group": "1W",
#     "year": 2002,
#     "year_add_vuz": 2020
# }
# class Student:
#     now_year = datetime.now().year
#
#     def __init__(self, name: str, group: str, age: int, course: int):
#         self.name = name
#         self.group = group
#         self.age = age
#         self.course = course
#
#     @classmethod
#     def the_name_of_def(cls, my_dict_: dict):
#         year = my_dict_.pop('year')
#         year_add_vuz = my_dict_.pop("year_add_vuz")
#         my_dict_.update({
#             "age": cls.now_year - year,
#             "course": cls.now_year - year_add_vuz
#         })
#         return cls(**my_dict_)
#
#     @staticmethod
#     def solving(course):
#         now_year = datetime.now().year
#         return now_year - course
#
#     def get_info(self):
#         print(self.name, self.age, self.course, self.group)
#
#
# syimyk = Student("Syimyk", "PMI3", 18, 1)
# arsen = Student.the_name_of_def(my_dict)
# syimyk.get_info()
# arsen.get_info()


