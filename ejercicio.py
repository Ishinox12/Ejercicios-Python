def nivel1():
    while True:
        print("\n=== Nivel 1: Basicos ===")
        print("1. Hola Mundo")
        print("2. Mostrar nombre")
        print("3. Suma de dos numeros")
        print("4. Area de triangulo")
        print("5. Celsius a Fahrenheit")
        print("6. Par o Impar")
        print("7. Mayor de tres numeros")
        print("8. Cuadrado de un numero")
        print("9. Tabla de multiplicar")
        print("10. Palabra al reves")
        print("0. Volver al menu principal")
        op = input("Elige una opcion: por favor:) ")
        
        if op == "1":
            print("Hola Mundo")
        elif op == "2":
            nombre = input("Nombre: ")
            print("Hola,", nombre)
        elif op == "3":
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("El resultado de la suma es:", a + b)
        elif op == "4":
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            area = (base * altura) / 2
            print("El area del triangulo es:", area)
        elif op == "5":
            c = float(input("Ingrese la temperatura en Celsius: "))
            print("Fahrenheit:" , (c * 9/5) + 32)
        elif op == "6":
            n = int(input("Ingrese un numero: "))
            print("El numero es par " if n % 2 == 0 else "El numero es impar")
        elif op == "7":
            x = float(input("Ingrese el primer numero: "))
            y = float(input("Ingrese el segundo numero: "))
            z = float(input("Ingrese el tercer numero: "))
            print("El mayor es:" , max(x, y, z))
        elif op == "8":
            n = float(input("Ingrese un numero: "))
            print("El cuadrado es:", n ** 2)
        elif op == "9":
            n = int(input("Ingrese un numero: "))
            print("Tabla de multiplicar de", n)
            for i in range(1, 11):
                print(n, "x", i, "=", n * i)
        elif op == "10":
            palabra = input("Ingrese una palabra: ")
            print("La palabra al reves es:", palabra[::-1])
        elif op == "0":
            break
        else:
            print("Opcion no valida, intente de nuevo plis .-.")
            
def nivel2():
    while True:
        print("\n=== Nivel 2: Estructuras de Control ===")
        print("11. Mayor o menor de Edad")
        print("12. Factorial")
        print("13. Promedio de 5 numeros")
        print("14. Numeros pares hasta n")
        print("15. Vocal o Consonante")
        print("16. Series Fibonacci (20 numeros)")
        print("17. Numero primo")
        print("18. Multiplos de 5 (1-100)")
        print("19. Contar vocales  en palabra")
        print("20. Calculadora")
        print("0. Volver al menu principal")
        op = input("Elige una opcion: por favor:) ")
        
        if op == "11":
            edad = int(input("Ingrese su edad: "))
            print("Eres mayor de edad" if edad >= 18 else "Eres menor de edad")
        elif op == "12":
            n = int(input("Ingrese un numero: "))
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i
            print("El factorial de", n, "es:", factorial)
        elif op == "13":
            suma = 0
            for i in range(5):
                suma += float(input(f"Ingrese el numero {i + 1}: "))
            print("El promedio es:", suma / 5)
        elif op == "14":
            n = int(input("Ingrese un numero: "))
            for i in range(2, n + 1, 2): 
                print(i, end=" ")
            print()
        elif op == "15":
            letra = input("Ingrese una letra: ").lower()
            print("Vocal" if letra in 'aeiou' else "Consonante")
        elif op == "16":
            a, b = 0, 1
            for i in range(20):
                print(a, end=" ")
                a, b = b, a + b
            print()
        elif op == "17":
            n = int(input("Ingrese un numero: "))
            es = True
            if n < 2:
                es = False
            else:
                for i in range(2, int(n ** 0.5) + 1):
                    if n % i == 0:
                        es = False
                        break
            print("Es primo" if es else "No es primo")
        elif op == "19":
            palabra = input("Ingrese una palabra: ").lower()
            print("Numero de vocales:", sum(1 for letra in palabra if letra in 'aeiou'))
        elif op == "20":
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            op2 = input("Ingrese la operacion (+, -, *, /): ")
            if op2 == "+": print(a+b)
            elif op2 == "-": print(a-b)
            elif op2 == "*": print(a*b)
            elif op2 == "/": print(a/b if b != 0 else "Error: Division por cero")
            else: print("Operacion no valida, Intentalo de nuevo plis :) ")
        elif op == "0":
            break
        else:
            print("Opcion no valida, intente de nuevo plis .-.")
            
def nivel3():
    while True:
        print("\n=== Nivel 3: Listas y Cadenas ===")
        print("21. Mayor de una lista")
        print("22. Ordenar lista")
        print("23. Eliminar duplicados")
        print("24. Ordenar nombres alfabeticamente")
        print("25. Suma de lista")
        print("26. Unir dos listas")
        print("27. Contar palabras en frase")
        print("28. Palindromo")
        print("29. Cuadrados de 10 primeros numeros")
        print("30. Segundo mayor de una lista")
        print("0. Volver al menu principal")
        op = input("Elige una opcion: por favor:) ")
        
        if op == "21":
            lista = [3,9,12,4,7,15,8,1,20,6]
            print("El mayor es:", max(lista))
        elif op == "22":
            lis = [9,3,7,1,6,4] 
            lis.sort()
            print("Lista ordenada:", lis)
        elif op == "23":
            lista = [1,2,3,4,4,5]
            print("Lista sin duplicados:", list(set(lista)))
        elif op == "24":
            nombres = ["Carlos", "Ana", "Pedro", "Luis"]
            nombres.sort()
            print("Nombres ordenados:", nombres)
        elif op == "25":
            lista = [1,2,3,4,5]
            print("La suma es:", sum(lista))
        elif op == "26":
            a = [1,2,3]
            b = [4,5,6]
            print("Listas unidas:", a + b)
        elif op == "27":
            frase = input("Ingrese una frase: ")
            print("Numero de palabras:", len(frase.split()))
        elif op == "28":
            palabra = input("Ingrese una palabra: ").lower()
            print("Es palindromo" if palabra == palabra[::-1] else "No es palindromo")
        elif op == "29":
            print("Cuadrados de los 10 primeros numeros:", [x**2 for x in range(1, 11)])
        elif op == "30":
            lista = [10,20,5,30,25]
            lista.sort()
            print("El segundo mayor es:", lista[-2])
        elif op == "0":
            break
        else:
            print("Opcion no valida, intente de nuevo plis .-.")
            
#Menu principal
def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Nivel 1: Basicos")
        print("2. Nivel 2: Estructuras de Control")
        print("3. Nivel 3: Listas y Cadenas")
        print("0. Salir")
        op = input("Elige una opcion: por favor:) ")
        
        if op == "1":
            nivel1()
        elif op == "2":
            nivel2()
        elif op == "3":
            nivel3()
        elif op == "0":
            print("Gracias por usar el programa. Adios! Sayonara :) ")
            break
        else:
            print("Opcion no valida, intente de nuevo plis .-.")