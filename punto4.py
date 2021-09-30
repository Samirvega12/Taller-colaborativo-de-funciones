cond="si"
def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True
while cond == "si":
    numero=int(input("ingrese un Número: "))
    if primo(numero):
        print("Es primo")
    else:
        print("No es primo")
    cond=input("¿quieres ingresar otro Número? ")
    if cond == "no":
        print("hasta luego, vuelva pronto.")
