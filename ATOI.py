s = "2+2"
sum = 0
s = [x for x in s]
le = len(s) - 1
for i in range(0, len(s), 1):
    if s[i] == "0":
        sum += 0 * (10 ** (le - i))
    if s[i] == "1":
        sum += 1 * (10 ** (le - i))
    if s[i] == "2":
        sum += 2 * (10 ** (le - i))
    if s[i] == "3":
        sum += 3 * (10 ** (le - i))
    if s[i] == "4":
        sum += 4 * (10 ** (le - i))
    if s[i] == "5":
        sum += 5 * (10 ** (le - i))
    if s[i] == "6":
        sum += 6 * (10 ** (le - i))
    if s[i] == "7":
        sum += 7 * (10 ** (le - i))
    if s[i] == "8":
        sum += 8 * (10 ** (le - i))
    if s[i] == "9":
        sum += 9 * (10 ** (le - i))
print(sum)

