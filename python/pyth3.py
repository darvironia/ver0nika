import time 
import os
import random as r
from module import hi as h, add as a
try:
    import nomodule
except ImportError:
    print ("Модуля nomodule  не существует")

h ()
print (a(45, 15))