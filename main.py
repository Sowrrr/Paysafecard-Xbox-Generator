import os, time, fade, random
from colorama import Fore
from pystyle import *
import string


# FORE COLORS
w = Fore.LIGHTWHITE_EX
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
b = Fore.LIGHTBLUE_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
black = Fore.LIGHTBLACK_EX




# DEFS

def slow_print(msg):
    for char in msg:
        print(char, end='', flush=True)
        time.sleep(0.5/30)

def generate_xbox_codigo():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    codigo = ""
    for i in range(25):
        if i % 5 == 0 and i > 0:
            codigo += "-"
        codigo += random.choice(letras)
    return codigo







os.system('cls')
os.system('title Sowrrr ^| Broken heart')





rotomicora=r"""
                 
     ,;;;;;;\     ,;;;;;;,        ╔╗╔╔═╗═╗ ╦╦╦ ╦╔═╗
   ,;;;@@@@@/   /;;@@@@@;;;,      ║║║║ ║╔╩╦╝║║ ║╚═╗
  ,;;;@@,;;;\   \,@,;;;,@@;;;,    ╝╚╝╚═╝╩ ╚═╩╚═╝╚═╝
  ;;;@@;;;' '\   \;' ';;;@@;;;          
  ;;;@@;;;   /   /    ;;;@@;;;    [1] Generate xbox codes
   ;;;@@';;, \   \  ,;;'@@;;;     
    ';;;@@';;,\   \;;'@@;;;'      [2] Generate paysafecard codes
      ';;;@@';/   /'@@;;;'       
        ';;;@/   /@@;;;' 
          ';/   /;@;;'           
                \;'
"""      




faded_rotomicora=fade.greenblue(rotomicora)
print(faded_rotomicora)
def choices():
    while True:
        choice = input(f"{b}[{y}>>>{b}] {r}Select generator {y}-{b}>{b} {black}")


        if choice == "1":
            os.system("cls")
            slow_print(f"{b}[{y}+{b}] {r}Loading{y}... {black}")
            time.sleep(3)
            os.system("cls")
            slow_print(f"{b}[{y}+{b}] {r}Generating xbox codes{y}...{black}")
            os.system('cls')
            letras = string.ascii_uppercase + string.digits
            while True:
                codigo = generate_xbox_codigo()
                with open("xbox-codes.txt", "a+") as f:
                    f.write(f"{codigo}\n")
                print(f"    {b}[{y}>{b}] {r}Code Generated {y}--{b}>{b}   {black}{codigo} \n")

        elif choice == "2":
            os.system('cls')
            slow_print(f"{b}[{y}+{b}] {r}Loading... {black}")
            time.sleep(3)
            os.system("cls")
            slow_print(f"{b}[{y}+{b}] {r}Generating paysafecard codes{y}... {black}")
            time.sleep(2)
            os.system('cls')
            letras = string.ascii_uppercase + string.digits
            while True:
                codigo2 = ""
                for i in range(1, 5):
                    codigo2 += ''.join(random.choice(letras) for i in range(4))
                if i < 4:
                    codigo2 += "-"
                f = open("paysafecard-codes.txt","a+")
                f.write(f"{codigo2}\n")
                print(f"    {b}[{y}>{b}] {r}Code Generated {y}--{b}>{b}   {black}{codigo2} \n")
choices()
