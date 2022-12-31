import math
import tkinter as tk
from threading import Thread
import tcas
from aircraft import AircraftCategory, Advisory
from tcas import Tcas

UI_SIZE = 500
UI_BUTTONS_BORDER = 50
UI_BUTTON_SIZE = 3
UI_DISPLAY_RANGE = tcas.TCAS_MAX_DISTANCE  # km

CANVAS_SIZE = (UI_SIZE - 2 * UI_BUTTONS_BORDER)
button_segment = CANVAS_SIZE / 5
spacer = UI_BUTTONS_BORDER / 4

class UI(Thread):

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("MSFS BVR")
        self.root.geometry(f"{UI_SIZE}x{UI_SIZE}")
        self.canvas = tk.Canvas(self.root, width=UI_SIZE, height=UI_SIZE, bg="darkgrey")
        self.canvas.create_rectangle(UI_BUTTONS_BORDER, UI_BUTTONS_BORDER, UI_SIZE-UI_BUTTONS_BORDER, UI_SIZE-UI_BUTTONS_BORDER, fill="black")
        self.canvas.pack()
        self.buttons = []


        ButtonFunctionMap = {}

        for i in range(0, 20):
            ButtonFunctionMap[i] = self.Pass
            text = ""
            x=0
            y=0
            if (i / 5.0) < 1:
                text = "—"
                x = UI_BUTTONS_BORDER * 0.25
                y = UI_BUTTONS_BORDER * 0.75 + button_segment * ((i % 5) + 0.5)
            elif (i / 5.0) < 2:
                text = "—"
                x = UI_SIZE - UI_BUTTONS_BORDER * 0.75
                y = UI_BUTTONS_BORDER * 0.75 + button_segment * ((i % 5) + 0.5)
            elif (i / 5.0) < 3:
                text = "|"
                x = UI_BUTTONS_BORDER * 0.75 + button_segment * ((i % 5) + 0.5)
                y = UI_BUTTONS_BORDER * 0.25
            elif (i / 5.0) < 4:
                text = "|"
                x = UI_BUTTONS_BORDER * 0.75 + button_segment * ((i % 5) + 0.5)
                y = UI_SIZE - UI_BUTTONS_BORDER * 0.75

            button = tk.Button(self.root, width=2, height=1, text=text, command=ButtonFunctionMap[i])
            button.place(x=x, y=y)

            self.buttons.append(button)
            ButtonFunctionMap[19] = self.onClick

            self.printLabel("test")

    def onClick(self, index):
        print(index)
        pass

    def Pass(self):
        pass

    def printLabel(self, text, index=-1):
        x = y = 0
        if index == -1:
            x = CANVAS_SIZE/2
            y = CANVAS_SIZE/2
        

        label = self.canvas.create_text(x, y, fill="green", font="Consolas 16", text=text)

    def run(self):
        self.root.mainloop()