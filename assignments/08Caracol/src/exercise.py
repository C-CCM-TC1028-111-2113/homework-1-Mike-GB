def main():
    #escribe tu código abajo de esta línea
    import math
    minutos = float(input("Dame los minutos: "))
    segundos = minutos*60
    cm = segundos*(5.7)
    conversion = cm/10
    print("Centímetros recorridos:", conversion)

if __name__ == '__main__':
    main()
