#Дебильный калькулятор v2

from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.BLUE)
print(Back.LIGHTGREEN_EX)

what = input( "Чо делаем? (+, -): " )

print (Back.LIGHTMAGENTA_EX)
a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))

print(Back.LIGHTCYAN_EX)
if what == "+":
    c = a + b
    print ("Результат:" + str(c))

elif what == "-":
    c = a - b
    print ("Результат:" + str(c))

else:
    print("Выбрана неверная операция!")
