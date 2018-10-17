#Autor: Claudio Mayoral García
#Descripción: Es un programa donde das el divisoy y el dividendo regresa el cociente y el residuo
# además. tiene otra función donde a partir de una lista de números menciona cual es el valor más alto.


#Esta función recibe los valores del divisoy y el dividendo e imprime el cociente con el residuo
def dividir(dividendo, divisor):
    primerValor = dividendo
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    residuo = dividendo
    print("%d / %d = %d, sobra %d" % (primerValor, divisor, cociente, residuo))
    print("")


#Esta función recibe una lista de números y regresa el número máximo
def encontrarMayor():
    numeroMayor = 0
    print("Teclea una serie de números para encontrar el mayor.")
    numero = 0
    while numero != -1:
        numero = int(input("Teclea un numero [-1 para salir]: "))
        if numero > numeroMayor:
            numeroMayor = numero
        elif numero < numeroMayor:
            numeroMayor = numeroMayor
    if numero == numeroMayor and numero == 0:
        print("No hay número mayor")
        print("")
    if numero == -1 and numeroMayor == 0:
        print("No hay número mayor")
        print("")
    if numeroMayor > 0:
        print("El mayor es: ", numeroMayor)
        print("")


#Función principal
def main():
    opcion = 0
    while opcion != 3:
        print("Mision 07. Ciclos while")
        print("Autor: Claudio Mayoral García")
        print("Matrícula: A01747749")
        print("1. Calcular divisiones")
        print("2. Encontrar el mayor")
        print("3. Salir")
        opcion = int(input("Teclea tu opción: "))
        print("")
        if opcion == 1:
            print("Calculando divisiones")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor)
        elif opcion == 2:
            encontrarMayor()
        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto.")
        else:
            print("ERROR, Teclea 1, 2 o 3")
            print("")


#Llama a la función principal
main()