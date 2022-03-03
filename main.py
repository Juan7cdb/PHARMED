from curses import window
from Pharmed import medicine_super_list
from tkinter import *


def run():
    window = Tk()
    window.title("PHARMED")
    window.geometry("400x400")
    window.mainloop()


if __name__ == "_main__":
    run()