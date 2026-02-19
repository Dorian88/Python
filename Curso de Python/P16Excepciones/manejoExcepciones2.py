#Manejando la clausula finally
def division():
    try:
        op1 = (float(input("Introduce el primer número: ")))
        op2 = (float(input("Introduce el segundo número: ")))
        print ("La división es: ", str(op1 / op2))
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    finally:
        print("Calculo finalizado")

division()