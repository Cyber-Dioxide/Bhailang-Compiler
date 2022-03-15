import random

from colorama import Fore , Back

W = Fore.LIGHTWHITE_EX
C = Fore.CYAN
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW

logo = """
  ______   ______   .___  ___. .______    __   __       _______ .______          __  
 /      | /  __  \  |   \/   | |   _  \  |  | |  |     |   ____||   _  \        |  | 
|  ,----'|  |  |  | |  \  /  | |  |_)  | |  | |  |     |  |__   |  |_)  |       |  | 
|  |     |  |  |  | |  |\/|  | |   ___/  |  | |  |     |   __|  |      /        |  | 
|  `----.|  `--'  | |  |  |  | |  |      |  | |  `----.|  |____ |  |\  \----.   |__| 
 \______| \______/  |__|  |__| | _|      |__| |_______||_______|| _| `._____|   (__) 
                                                                                     
"""

for i in logo:
        ran_col = random.choice([W , C , R , G , Y])
        print(ran_col + i , end="")


def version():
    RB = Back.RED
    print(RB + W +"version: 1.0.0 BETA" + Back.RESET + Fore.RESET)

