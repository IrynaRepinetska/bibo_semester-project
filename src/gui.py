import tkinter as tk

def Enter_pressed(event):
    """Took the current string in the Entry field."""
    input_get = input_field.get()
    verlauf.insert('end',input_get + '\n') #Hier die Ausgabe des Bots mit einbauen
    input_field.delete(0,'end')


window = tk.Tk()
window.configure(background='white')


scroll = tk.Scrollbar(window)
verlauf = tk.Text(window, height=40, width=tk.maximize)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
verlauf.pack(side=tk.TOP, fill=tk.Y)
scroll.config(command=verlauf.yview)
verlauf.config(yscrollcommand=scroll.set)

input_user = tk.StringVar()
input_field = tk.Entry(window, text=input_user)
input_field.pack()



input_field.bind("<Return>", Enter_pressed)
window.mainloop()
