
def sumar(a, b):
    """Suma dos números"""
    return a + b
    
def calculadora():
    """Calculadora simple con 4 operaciones básicas"""
    print("=== CALCULADORA SIMPLE ===")
    print("1. Sumar")
    
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
            except ValueError:
                print("Error: Ingrese números válidos")
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    calculadora()
