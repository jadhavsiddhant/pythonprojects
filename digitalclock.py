from tkinter import Label, Tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, update_time)

root = Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.resizable(False, False)

clock = Label(root, font=("Arial", 48), bg="black", fg="white")
clock.pack(fill="both", expand=True)

update_time()
root.mainloop()
