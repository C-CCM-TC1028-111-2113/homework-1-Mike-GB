def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    mensajes = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))
    cobro = 0.80
    costo_total= (mensajes*cobro)+(megas*cobro)+(minutos*cobro)
    
    print("El costo mensual es: ", costo_total)


if __name__ == '__main__':
    main()
