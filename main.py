# Project: Micro Notes Edit
# Created: 04/01/2018
# Revised: 26/05/2022
# Version: 1.1
# License: MIT


from tkinter import PhotoImage
from tkinter import filedialog
from tkinter import *


main = Tk()
main.title("Micro Notes Edit")
main.config(bg="#282A36")


# Open file callback function
def open_file_callback():
    filename = filedialog.askopenfilename()
    if filename:
        file = open(filename, 'r')
        text_area.delete(0.0, END)
        text_area.insert(0.0, file.read())
        file.close()


# Save file callback function
def save_file_callback():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Documentos de texto (*.txt)", "*.txt"),))
    if filename:
        file = open(filename, 'w')
        file.write(text_area.get(0.0, END))
        file.close()


# Menu label
lm = Label(main, bg="#282A36")
lm.grid(row=0, column=1, sticky="W, E")
main.grid_columnconfigure(1, weight=1) 


# Spacing label
spacing_label1 = Label(lm, bg="#282A36")
spacing_label1.grid(row=0, column=0)     


# Open button
btn_open = Label(lm, text="Open", font=("helvetica", "12"), fg="#fff", background="#282A36", cursor="tcross")
btn_open.grid(row=0, column=1)
btn_open.bind("<Button-1>", lambda e: open_file_callback())


# Spacing label
spacing_label2 = Label(lm, bg="#282A36")
spacing_label2.grid(row=0, column=2)                              


# Save button                           
btn_save = Label(lm, text="Save", font=("helvetica", "12"), fg="#fff", background="#282A36", cursor="tcross")
btn_save.grid(row=0, column=3)
btn_save.bind("<Button-1>", lambda e: save_file_callback())                     


# Text area
text_area = Text(main, background="#44475A", fg="#fff", insertbackground="#fff", highlightbackground="#282A36", padx="4", pady="3", bd="0")
text_area.grid(row=2, column=1, sticky="N, E, S, W")


# Scrollbar
scrollbar = Scrollbar(main, bg="#282A36", activebackground="#282A36", elementborderwidth="0", troughcolor="#44475A", bd="0")
scrollbar.grid(row=2, column=2, sticky="N, S")


# Text area and Scrollbar configs
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)


# Window configs
main.grid_rowconfigure(2, weight=1)
main.geometry("660x490+100+80")
main.mainloop()
