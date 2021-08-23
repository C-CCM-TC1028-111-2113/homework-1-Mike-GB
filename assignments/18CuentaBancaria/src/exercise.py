def main():
    #escribe tu código abajo de esta línea
    mes_anterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = float(input("Dame el número de cheques: "))
    
    saldo = mes_anterior + ingresos - egresos - 13*cheques
    saldo_final = saldo - (0.075)*saldo
    print("El saldo final de la cuenta es:", saldo_final)
    

if __name__ == '__main__':
    main()
