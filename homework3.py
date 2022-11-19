
#Задание 1
lst = [5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8]
lst = list(dict.fromkeys(lst))
lst.sort()
lst.extend([[3, 5, 6, 8, 13, 15]])
print(lst)

#Задание 2
# newString = "72 101 108 108 111"
# result = ""
# for x in newString.split():
#     result = result + chr(int(x))
# print(result)


#Задание 3
# tryCount = 1
# def Main():
#     global tryCount
#     if tryCount <= 3:
#         print('Добро пожаловать в регистрацию')
#         nickName = input("Введите свой никнейм: \n")
#         if "@" in nickName or "/" in nickName:
#             tryCount = tryCount + 1
#             print('Неверный никнейм.')
#             if tryCount <= 3:
#                 print('Попробуйте снова.')
#             Main()
#         else:
#             password = input("Введите пароль: \n")
#             repeatPassword = input("Подтвердите пароль: \n")
#             if password and repeatPassword and repeatPassword != password:
#                 print('Пароли не совпадают.')
#                 tryCount = tryCount + 1
#                 if tryCount <= 3:
#                     print('Попробуйте снова.')
#                 Main()
#             else:
#                 print('Регистрация завершена успешно.')
#                 tryCount = 1
#     else:
#         print('В регистрации отказано.')

# Main()