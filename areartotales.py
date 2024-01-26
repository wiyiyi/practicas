##calcular el area total 
import time
import math 
lado=10
radio=5
base=10
altura=10
print("Holi")
def areaCuadrado(lado):
    print ("calculando area de cuadrado...")
    time.sleep(2)
    return lado*lado
def areacirculo(radio):
     return math.pi*radio**2
def areatriangulo(base,altura):
     return base*altura/2
def areamedio (lado):
     return base*lado/2
areatotal=areaCuadrado(lado)+areacirculo(radio)+areatriangulo(base,altura)+areamedio(lado)
print(areatotal)
