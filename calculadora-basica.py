def calculadora():
  print("Bienvenido a la calculadora básica")
  
  while True:
    operacion = input("Elige una operación (+, -, *, /) o 'salir' para terminar: ")
    if operacion == 'salir':
      break
    
    if operacion in ['+', '-', '*', '/']:
      try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if operacion == '+':
          print(f"Resultado: {num1 + num2}")
        elif operacion == '-':
          print(f"Resultado: {num1 - num2}")
        elif operacion == '*':
          print(f"Resultado: {num1 * num2}")
        elif operacion == '/':
          print(f"Resultado: {num1 / num2}")
      except ValueError:
        print("Por favor, ingresa números válidos.")
    else:
      print("Operación no válida. Inténtalo de nuevo.")
        
calculadora()