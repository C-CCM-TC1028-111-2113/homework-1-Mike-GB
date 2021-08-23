def main():
    #escribe tu código abajo de esta línea
    import math
    num_palabras = int(input("Dame el número de palabras: "))
    
    paginas = math.ceil(num_palabras/475)
    costo = paginas*60 - 0.1*(paginas*60)
    
    print("El costo de la publicación es:", costo)


if __name__ == '__main__':
    main()
