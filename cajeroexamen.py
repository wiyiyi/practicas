## elaborar un cajero automatico
import time
c=100
opcion=0
contra=253
usuario=0
regreso =0
def bienvenida(usuario):
  usu=input("usuario:")
  print ("Bienvenido al cajero",usu)
bienvenida(usuario)

contraseña=int (input("contraseña:"))

while contraseña!=contra:
    time.sleep(1)
    print ("intente nuevamente...")
    time.sleep(1)
    contraseña=int (input("contraseña:"))
  
if contraseña==contra:
  
  print ("contraseña exitosa")
  time.sleep(1)
  print ("acceciendo al sistema...")
  time.sleep(1)
    ##############################################

  def deposito (c):
   time.sleep(1)
   depo= int(input("deposita:"))
   Depo=c+depo
   print("saldo actual:",Depo)
   time.sleep(1)
   return ("deposito exitoso")
   
   
  def retiro(c):
      reti=int(input("retira:"))
      Reti=c-reti
      print("saldo actual:",Reti)
      return "retiro exitoso"
  def consulta(c):
     return ("consultando saldo")
  print ("Su saldo es de",c)
   

def Menu():
 def transacion(opcion):
     opcion=int (input("opcion:"))
     if opcion==1:
      print (deposito(c))
     if opcion==2:
      print(retiro(c))
     if opcion==3:
      time.sleep(1)
      print(consulta(c))
      time.sleep(1)
 transacion(opcion)
Menu()





 