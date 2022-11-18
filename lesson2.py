# инкапсуляция
# private protected public

# class Product:
#     def __init__(self, name: str, price: int):
#         self.name = name
#         self.price = price
#
#     def get_info(self):
#         print(f'{self.name} - {self.price}')
#
# potato = Product("potato", 25)
# potato.get_info()


# import uuid
# class Bank:
#     def __init__(self, name: str):
#         self.name = name
#         self.__generate_account()
#
#     def __generate_account(self):
#         self.account = str(uuid.uuid4())
#
#     def get_account(self):
#         print(f'Ввш аккаунт {self.account}')
#
#     def set_account(self):
#         self.__acount = str(uuid.uuid4()) + self.name
#
#
# arsen = Bank('Aabesov')
# arsen.get_account()
# arsen.set_account()
# arsen.get_account()


import string

# usernames_list = ["pro100", "qwerty", "arsen", "sadq"]
# email_test = ["gmail.com", "outlook.com", "mail.ru"]


# class Registration:
#     def __init__(self, username: str, password: str, email: str):
#         self.save(username, password, email)
#
#     def username_validate(self, username):
#         if username in usernames_list:
#             raise Exception("Username Error")
#         return True
#
#     def password_validate(self, password):
#         if len(password) < 8 or password.isalpha() or password.isdigit() or password[0].islower():
#             raise Exception("Пароль должен содержать не менее 8 символов включая символы и числа")
#         return True
#
#     def email_validate(self, email):
#         for i in email_test:
#             if "@" in email and email.endswith(i):
#                 return True
#         raise Exception("Email error")
#
#     def save(self, username, password, email):
#         if (self.username_validate(username) and self.password_validate(password) and self.email_validate(email)):
#             usernames_list.append(username)
#             self.username = username
#             self.password = password
#             self.email = email
#
#
# arsen = Registration("lopppol", "Kasj19y1d2", "aabesov@mail.ru")
# # print(usernames_list)
