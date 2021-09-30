def sumaDigitos(numero): 
    suma=0 
    while numero!=0:  
        digito=numero%10 
        suma=suma+digito 
        numero=numero//10 
    return suma 
sumatoria=0 
num=int(input("Número a procesar,ingrese 0 para terminar: ")) 
while num!=0: 
    print("Suma:",sumaDigitos(num)) 
    sumatoria=sumatoria+num 
    num=int(input("Número a procesar,ingrese 0 para terminar: ")) 
print("Sumatoria:", sumatoria) 
print("Dígitos:", sumaDigitos(sumatoria))
