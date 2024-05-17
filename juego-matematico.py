import random

def juego_de_matematicas():
  operaciones = ['+', '-', '*']
  
  print("¡Bienvenido al juego de matemáticas!")
  print("Responde las siguientes preguntas:")

  for _ in range(5):  # Genera 5 preguntas
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operacion = random.choice(operaciones)
    
    if operacion == '+':
      resultado_correcto = num1 + num2
    elif operacion == '-':
      resultado_correcto = num1 - num2
    elif operacion == '*':
      resultado_correcto = num1 * num2

    pregunta = f"¿Cuánto es {num1} {operacion} {num2}? "
    respuesta = int(input(pregunta))
    
    if respuesta == resultado_correcto:
      print("¡Correcto!")
    else:
      print(f"Incorrecto. La respuesta correcta es {resultado_correcto}.")
  
  print("¡Gracias por jugar!")

juego_de_matematicas()