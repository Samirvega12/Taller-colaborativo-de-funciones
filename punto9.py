cond="si"
def frecuencia(numero):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       cantidad+=1
       numero=numero//10
   return cantidad
while cond=="si":
    hi=input("""que desea ingresar:
    1.Cedula de ciudadania
    2.Tarjeta de identidad
      = """)
    num=int(input("ingrese el numero: "))
    if frecuencia(num)<4 and frecuencia(num)<12:
        print("el numero  es invalido")
    else:
        print("numero es valido")
        cond="no"
    cond=input("¿quieres volver a ingresar?= ¿si o no? ")
    if cond =="no":
        print("vuelve pronto amigo....(saludos desde Tibú)")
