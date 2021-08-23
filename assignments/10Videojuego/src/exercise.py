def main():
    #escribe tu código abajo de esta línea
    nuevos = int(input("Dame la cantidad de juegos nuevos: "))
    usados = int(input("Dame la cantidad de juegos usados: "))
    
    costo_n = (nuevos*1000)
    costo_u = (usados*350)
    
    costo_total = costo_n + costo_u

    print("El total de la compra es:", costo_total)

if __name__ == '__main__':
    main()
