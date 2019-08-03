from math import *

def help_():
    print("""1- PKR-USD
    2- USD-PKR
    3- GBP-PKR
    4- PKR-GBP
    5""")

while True:
    conv = int(input("Please enter your required exchange: "))
    if conv == 1:
        """PKR-USD"""
        pkr = float(input("PKR: "))
        usd = pkr * 0.0096
        print("USD: ", round(usd, 2))
    elif conv == 2:
        """USD-PKR"""
        usd = float(input("USD: "))
        pkr = usd * 104.69
        print("PKR: ", round(pkr, 2))
    elif conv ==
    
    w_t_con = input("Continue? Enter y or n: ")    # Whether to continue
    if w_t_con == "y":
        continue
        print('Restarting')
    elif w_t_con == "n":
        break
    else:
        print("Illegal value. RESTARTING...")
