print("las areas se calculan con...")

def infoCuadrado():
    print ("el area se calcula lado*lado")
infoCuadrado()

def infocuadrado():
    return"el area es lado*lado"
print(infocuadrado())

def infotriangulo():
    return"se calcula con base*altura/2"
print(infotriangulo())

def infopentagono():
    print("se calcula con perimetro*altura/2")
print(infopentagono())


def inforectangulo():
    return "se calcula con base*altura"
print(inforectangulo())


def menudefiguras(opcion):
 
    Opcion=int (input("di un numero:"))
    if Opcion==1:
     infoCuadrado()
    elif Opcion==2:
        print((infotriangulo))
    elif Opcion==3:
        infopentagono()
    elif Opcion==3:
        print(inforectangulo())
menudefiguras(opcion)
