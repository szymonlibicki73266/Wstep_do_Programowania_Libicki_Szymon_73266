x = int(input("podaj x: "))
y = int(input("podaj y: "))
z = int(input("podaj z: "))

if x >= y and x >= z:
    if y >= z:
        print(x,y,z)
    elif z >= y:
        print(x,z,y)
elif y >= x and y >= z:
    if x >= z:
        print(y,x,z)
    elif z >= x:
        print(y,z,x)
elif z >= x and z >= y:
    if x >= y:
        print(z,x,y)
    elif y >= x:
        print(z,y,x)
