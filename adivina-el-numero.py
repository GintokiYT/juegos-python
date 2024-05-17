import random

def adivina_el_numero():
  numero_secreto = random.randint(1, 100)
  intentos = 0
  
  print("¡Bienvenido al juego de adivinar el número!")
  print("Estoy pensando en un número entre 1 y 100.")
  
  while True:
    intento = int(input("Adivina el número: "))
    intentos += 1
    
    if intento < numero_secreto:
      print("Demasiado bajo.")
    elif intento > numero_secreto:
      print("Demasiado alto.")
    else:
      print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
      break

adivina_el_numero()