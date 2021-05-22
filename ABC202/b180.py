b = input()
c = ""
for i in reversed(b):
    if i == "6":
        c += "9"
    elif i == "9":
        c += "6"
    else:
        c += i
print(c)