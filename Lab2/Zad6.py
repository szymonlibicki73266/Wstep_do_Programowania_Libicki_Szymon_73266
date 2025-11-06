tresc = "Python jest super"

print(tresc[0])

print(tresc[-1])

for i in range(0, len(tresc), 2):
    print(tresc[i], end=" ")

for i in range(1, len(tresc), 3):
    print(tresc[i], end=" ")

for i in range(9, len(tresc)):
    print(tresc[i], end=" ")

for i in range(len(tresc)-1, -1, -1):
    print(tresc[i], end="")