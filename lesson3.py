# class Doctor:
#     def __init__(self, name, age, experience):
#         self.name = name
#         self.age = age
#         self.experience = experience
#
#     def heal(self):
#         print(f"{self.name} лечит")
#
#     def add_exp(self, year):
#         self.experience += year
#
#     def get_info(self):
#         return f"{self.name}, {self.age}, {self.experience}"
# # if add self.salary to method get_info in wouldn't work(FOR CLASS DOCTOR)
#
# class Dantist():
#     def __init__(self, spec):
#         self.spec = spec
#
#
# class OrtoDent(Dantist, Doctor):
#     def __init__(self, name, age, experience, spec, salary):
#         # super().__init__(name, age, experience)
#         Doctor.__init__(self, name, age, experience)
#         Dantist.__init__(self, spec)
#         self.salary = salary
#
#     def get_info(self):
#         all_info = Doctor.get_info(self) + f", {self.spec}, {self.salary}"
#         print(all_info)
#
#
# b = Doctor("Nurlan", 35, 15)
# # b.get_info()
# arsen = OrtoDent("ars", 17, 4, "bracket", 150000)
# arsen.get_info()


# class Append(tuple):
#     def append(self, my_tup):
#         my_list = list(self)
#         my_list.append(my_tup)
#         return tuple(my_list)
#
#
#
# arsen = Append("asdasfdsf")
# print(arsen.append([3, 4]))
