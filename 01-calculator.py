print("=============================")
print("     CALCULADORA BASICONA    ")
print("=============================")

while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    op = input("ingrese una opcion: ")

    if op == "5" or op == "SALIR":
        print("adios")
        break

    # if op == "1" or op == "2" or op == "3" or op == "4":
    #     n1 = float(input("Ingrese el primer numero: "))
    #     n2 = float(input("Ingrese el segundo numero: "))

    match op:
        case "1" | "2" | "3" | "4":
            try:
                n1 = float(input("Ingrese el primer numero: "))
                n2 = float(input("Ingrese el segundo numero: "))
            except ValueError:
                print("Error: Debe ingresar un valor numérico válido.")
                continue  # O reiniciar el ciclo

            match op:
                case "4":
                    if n2 == 0:
                        print("Error, no se puede dividir por 0")
                    
                    else:
                        resultado = n1 / n2
                        print(f"resultado: {resultado}")

                case "1":
                    resultado = n1+n2
                    print(f"resultado: {resultado}")

                case "2":
                    resultado = n1-n2
                    print(f"resultado: {resultado}")

                case "3":
                    resultado = n1*n2
                    print(f"resultado: {resultado}")
                
            
