from tkinter import *
from tkinter import ttk
import random

from snake_game import SnakeGame

# Aantal blokjes in de hoogte en breedte van het speelveld.
veld_grootte = 20

# De groote van een blokje op het scherm
vierkant_grootte = 25

def teken_slang(canvas, slang_posities):
    light_green = "#90ee90"
    canvas.create_rectangle(slang_posities[0][0] * vierkant_grootte,
                            slang_posities[0][1] * vierkant_grootte,
                            slang_posities[0][0] * vierkant_grootte + vierkant_grootte,
                            slang_posities[0][1] * vierkant_grootte + vierkant_grootte,
                            outline="white", fill=light_green)

    for i in range(1, len(slang_posities)):
        canvas.create_rectangle(slang_posities[i][0] * vierkant_grootte,
                                slang_posities[i][1] * vierkant_grootte,
                                slang_posities[i][0] * vierkant_grootte + vierkant_grootte,
                                slang_posities[i][1] * vierkant_grootte + vierkant_grootte,
                                outline="white", fill="green")


def teken_voedsel(canvas, voedsel_positie):
    canvas.create_rectangle(voedsel_positie[0] * vierkant_grootte,
                            voedsel_positie[1] * vierkant_grootte,
                            voedsel_positie[0] * vierkant_grootte + vierkant_grootte,
                            voedsel_positie[1] * vierkant_grootte + vierkant_grootte,
                            outline="white", fill="red")


def start_game(scherm, canvas):
    global game
    game = SnakeGame([(10, 10), (11, 10), (12, 10), (13, 10), (14, 10)], (15,15), veld_grootte)

    game_loop(scherm, canvas)


def game_loop(scherm, canvas):
    if (scherm):
        game.tick()

        if (not game.is_snake_dead()):
            # Verwijder alle getekende dingen op het scherm alvorens opnieuw te tekenen
            canvas.delete("all")
            teken_slang(canvas, game.get_snake_positions())
            teken_voedsel(canvas, game.get_food_position())
            canvas.pack(fill=BOTH, expand=1)

            # Roep na 150ms deze functie opnieuw op voor de volgende stap uit te voeren
            scherm.after(150, lambda: game_loop(scherm, canvas))
        else:
            # Toon Game over en Restart knop
            restart_knop = ttk.Button(canvas, text="Restart")
            restart_knop['command'] = lambda: start_pressed(scherm, canvas, restart_knop)
            restart_knop.pack()
            canvas.create_text(250, 200, fill="black", font="Times 20 italic bold",
                               text="Game over!")
            print("Game over")
            canvas.pack()


def start_pressed(screen, canvas, button):
    button.pack_forget()
    start_game(screen, canvas)


def toets_ingedrukt(event):
    global game
    if (event.keysym == "Up"):
        game.turn_snake_north()
    elif (event.keysym == "Right"):
        game.turn_snake_east()
    elif (event.keysym == "Down"):
        game.turn_snake_east()
    elif (event.keysym == "Left"):
        game.turn_snake_west()

scherm = Tk()
scherm.geometry(str(veld_grootte * vierkant_grootte) + "x" + str(veld_grootte * vierkant_grootte))
canvas = Canvas(scherm, width=veld_grootte * vierkant_grootte, height=veld_grootte * vierkant_grootte, bd=0,
                highlightthickness=0)
scherm.bind('<Key>', toets_ingedrukt)
start_knop = ttk.Button(canvas, text="Start")
start_knop['command'] = lambda: start_pressed(scherm, canvas, start_knop)
start_knop.pack()
canvas.pack()

scherm.mainloop()