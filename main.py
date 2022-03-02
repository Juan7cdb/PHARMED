from re import search
from Pharmed import run as pharmed
import tkinter as tk


def search():
    content = search_box.get()
    result = pharmed(content, pharmed)
    T.delete("1.0", tk.END)
    T.insert(tk.END, result)

  
def run():
    window = tk.Tk()
    window.title("PHAMED")
    window.geometry("300x300")
    search_box = tk.Entry(window)
    search_box.place(x=0,y=0)
    search_box.bind("<Return>", search)
    T = tk.Text(window)
    search_box.pack()
    T.pack()
    T.insert(tk.END, "Test")
    


if __name__ == "__main__":
    run()