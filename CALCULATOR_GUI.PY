import tkinter as tk

def click(event):
    global sc_value
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(sc_value.get())
            sc_value.set(result)
            screen.update()
        except Exception as e:
            sc_value.set("Error")
    elif text == "C":
        sc_value.set("")
    else:
        sc_value.set(sc_value.get() + text)
        screen.update()

root = tk.Tk()
root.title("Calculator")

sc_value = tk.StringVar()
sc_value.set("")
screen = tk.Entry(root, textvar=sc_value, font="lucida 20 bold")
screen.pack(fill="both", ipadx=8, padx=10, pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "+", "-", "*", "/", "C", "="
]

row = 0
col = 0
for button in buttons:
    btn = tk.Button(frame, text=button, font="lucida 15 bold")
    btn.grid(row=row, column=col, padx=10, pady=10)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        row += 1
        col = 0

root.mainloop()
