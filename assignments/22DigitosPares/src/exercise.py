def main():
    #escribe tu código abajo de esta línea
    number = int(input("Dame un número: "))
    lista = list(str(number))
    digitos= [int(x) for x in lista]
    par = 0
    for num in digitos:
        if num % 2 == 0:
            par += 1
        else:
            par+=0
    print("El número de dígitos pares es:", par)


if __name__ == '__main__':
    main()
