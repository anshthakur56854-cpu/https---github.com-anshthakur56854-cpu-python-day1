import tkinter as tk         #Tkinter import krna


window = tk.Tk()               # Window bnana

window.title("My First App")      # Window ka title
window.geometry("400x300")         # Window ka Size

lable = tk.Label(window , text ="Hello python")     # Window ka label bnana
lable.pack()                                      # Lable ko window me dikhana 

window.mainloop()                     # Window ko continuosly chalna



