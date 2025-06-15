# Importamos la librería random para generar la jugada aleatoria del computador
import random

# Mensaje de bienvenida
print(("---Bienvenido a Piedra, Papel o Tijera---"))

while True:
    try:
        print("Elije una opcion: \n1 = 🧱 Piedra\n2 = 📄 Papel\n3 = ✂️ Tijera\n0 = 🚪 Salir del juego")

        #Le pedrimos asl usuario que ingrese su jugada
        jugada = int(input("Ingrese su jugada: "))

        #Si escribe 0 sale del juego
        if jugada == 0:
            print("👋 Gracias por jugar. ¡Hasta luego!")
            break

        #Validamos la jugada del usuarui que este entre el 1 y el 3
        if jugada <1 or jugada > 3:
            print("❌ Jugada inválida. Ingresa 1, 2 o 3.")
            continue
        #la computadora genera una jugada aleatoria entre el 1 y el 3
        jugada_pc = random.randint(1,3)

        #Mostramos la jugade del usuario y de la pc
        print(f"Tu elegiste la jugada: {jugada}")
        print(f"La computadora eligio la jugada: {jugada_pc}")

        #Comparamos las jugadas
        if jugada == jugada_pc:
            print("🤝 Resultado: Empate")
        if (jugada == 1 and jugada_pc == 3) or\
              (jugada == 2 and jugada_pc == 1) or\
                  (jugada == 3 and jugada_pc == 2):
            print("🎉 Resultado: ¡Ganaste!")
        else:
            print("💀 Resultado: Perdiste")
    except ValueError:
         print("❗ Error: Solo puedes escribir números del 1 al 3 (o 0 para salir).")