import random

def piedra_papel_tijeras():
  opciones = ["piedra", "papel", "tijeras"]
  
  print("¡Bienvenido al juego de piedra, papel o tijeras!")
  
  while True:
    jugador = input("Elige piedra, papel o tijeras (o 'salir' para terminar): ").lower()
    if jugador == 'salir':
      break
    
    computadora = random.choice(opciones)
    print(f"Computadora eligió: {computadora}")
    
    if jugador == computadora:
      print("¡Es un empate!")
    elif (jugador == "piedra" and computadora == "tijeras") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijeras" and computadora == "papel"):
      print("¡Ganaste!")
    else:
      print("¡Perdiste!")
      
piedra_papel_tijeras()