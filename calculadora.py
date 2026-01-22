def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def calculadora():
    """Calculadora simple con 4 operaciones básicas"""
    print("=== CALCULADORA SIMPLE ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    while True:
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break
        
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                if opcion == '1':
                    resultado = sumar(num1, num2)
                    print(f"Resultado: {num1} + {num2} = {resultado}")
                elif opcion == '2':
                    resultado = restar(num1, num2)
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                elif opcion == '3':
                    resultado = multiplicar(num1, num2)
                    print(f"Resultado: {num1} × {num2} = {resultado}")
                elif opcion == '4':
                    resultado = dividir(num1, num2)
                    print(f"Resultado: {num1} ÷ {num2} = {resultado}")
            except ValueError:
                print("Error: Ingrese números válidos")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    calculadora()
