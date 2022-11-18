# dunder methods
# equal
# multiple
# division
# +, -, /, *


# class Point:
#
#     def __init__(self,x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"object x = {self.x}, y = {self.y}"
#
#     def __add__(self, other):
#         if isinstance(other, Point):
#             raise Exception(f"{other} является обьектом Point!!!")
#         result = self.x * self.y + other
#         return result
#
#     def __radd__(self, other):
#         if isinstance(other, Point):
#             raise Exception(f"{other} является обьектом Point!!!")
#         result = self.x * self.y + other
#         return result
#
#
# obj = Point(6, 3)
# obj1 = Point(9, 3)
# print(8 + obj1)
# # print(obj + obj1)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"object x = {self.x}, y = {self.y}"
#
#     def __mul__(self, other):
#
#
# obj = Point('6', '3')
# obj1 = Point(9, 3)
# print(obj + 8)