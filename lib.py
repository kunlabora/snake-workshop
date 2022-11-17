from snake_game import SnakeGame
from tkinter import *
from tkinter import ttk

class SnakeRunner:
    veld_grootte = 20
    vierkant_grootte = 25

    def __init__(self):
        self.game = None

    def teken_slang(self, canvas, slang_posities):
        light_green = "#90ee90"
        canvas.create_rectangle(slang_posities[0][0] * self.vierkant_grootte,
                                slang_posities[0][1] * self.vierkant_grootte,
                                slang_posities[0][0] * self.vierkant_grootte + self.vierkant_grootte,
                                slang_posities[0][1] * self.vierkant_grootte + self.vierkant_grootte,
                                outline="white", fill=light_green)

        for i in range(1, len(slang_posities)):
            canvas.create_rectangle(slang_posities[i][0] * self.vierkant_grootte,
                                    slang_posities[i][1] * self.vierkant_grootte,
                                    slang_posities[i][0] * self.vierkant_grootte + self.vierkant_grootte,
                                    slang_posities[i][1] * self.vierkant_grootte + self.vierkant_grootte,
                                    outline="white", fill="green")


    def teken_voedsel(self, canvas, voedsel_positie):
        canvas.create_rectangle(voedsel_positie[0] * self.vierkant_grootte,
                                voedsel_positie[1] * self.vierkant_grootte,
                                voedsel_positie[0] * self.vierkant_grootte + self.vierkant_grootte,
                                voedsel_positie[1] * self.vierkant_grootte + self.vierkant_grootte,
                                outline="white", fill="red")


    def start_game(self, scherm, canvas):
        self.game = SnakeGame([(10, 10), (11, 10), (12, 10), (13, 10), (14, 10)], (15,15), self.veld_grootte)

        self.game_loop(scherm, canvas)


    def game_loop(self, scherm, canvas):
        if (scherm):
            self.game.tick()

            if (not self.game.is_snake_dead()):
                # Verwijder alle getekende dingen op het scherm alvorens opnieuw te tekenen
                canvas.delete("all")
                self.teken_slang(canvas, self.game.get_snake_positions())
                self.teken_voedsel(canvas, self.game.get_food_position())
                canvas.pack(fill=BOTH, expand=1)

                # Roep na 150ms deze functie opnieuw op voor de volgende stap uit te voeren
                scherm.after(150, lambda: self.game_loop(scherm, canvas))
            else:
                # Toon Game over en Restart knop
                restart_knop = ttk.Button(canvas, text="Restart")
                restart_knop['command'] = lambda: self.start_pressed(scherm, canvas, restart_knop)
                restart_knop.pack()
                canvas.create_text(250, 200, fill="black", font="Times 20 italic bold",
                                   text="Game over!")
                print("Game over")
                canvas.pack()


    def start_pressed(self, screen, canvas, button):
        button.pack_forget()
        self.start_game(screen, canvas)


    def toets_ingedrukt(self, event):
        if (event.keysym == "Up"):
            self.game.turn_snake_north()
        elif (event.keysym == "Right"):
            self.game.turn_snake_east()
        elif (event.keysym == "Down"):
            self.game.turn_snake_east()
        elif (event.keysym == "Left"):
            self.game.turn_snake_west()

    def run_snake(self):
        scherm = Tk()
        scherm.geometry(str(self.veld_grootte * self.vierkant_grootte) + "x" + str(self.veld_grootte * self.vierkant_grootte))
        canvas = Canvas(scherm, width=self.veld_grootte * self.vierkant_grootte, height=self.veld_grootte * self.vierkant_grootte, bd=0,
                        highlightthickness=0)
        scherm.bind('<Key>', self.toets_ingedrukt)
        start_knop = ttk.Button(canvas, text="Start")
        start_knop['command'] = lambda: self.start_pressed(scherm, canvas, start_knop)
        start_knop.pack()
        canvas.pack()

        scherm.mainloop()