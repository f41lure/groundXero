# Currency exchange ranges

unit = raw_input("What to convert into: ")



if unit == "$" or unit == "dollars":
    amount = int(input("USD: "))
    pkr = amount * 104.29
    print(pkr)
