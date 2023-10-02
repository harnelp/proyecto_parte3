import os
import keyboard

def clear_and_print(num):
    # Limpiamos la terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # Imprimimos el número
    print(num)

num = 0
while num <= 50:
    # Si se presiona la tecla 'n'
    if keyboard.is_pressed('n'):
        num += 1
        clear_and_print(num)