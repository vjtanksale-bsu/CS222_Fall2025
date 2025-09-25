import tkinter as tk
from tkinter import ttk
def submit():
    selected = combo.get()
    lblResult.config(text=f"You selected: {selected}")
window = tk.Tk()
window.title("ComboBox Example")
window.geometry("300x200")
combo = ttk.Combobox(window)
combo['values'] = ("IN", "OH", "MI")
btnSubmit = tk.Button(window, text="Submit", command=submit)
lblResult = tk.Label(window, text="")
combo.grid(column=0, row=0)
btnSubmit.grid(column=1, row=0)
lblResult.grid(column=0, row=1)
window.mainloop()