from tkinter import *

def calculate_si():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        si = (principal * rate * time) / 100
        result_label.config(text=f"Simple Interest: {si:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")


root = Tk()
root.title("Simple Interest Calculator")
root.geometry("300x300")

Label(root, text="Principal (P):").pack()
principal_entry = Entry(root)
principal_entry.pack()

Label(root, text="Rate of Interest (R%):").pack()
rate_entry = Entry(root)
rate_entry.pack()

Label(root, text="Time (T in years):").pack()
time_entry = Entry(root)
time_entry.pack()

Button(root, text="Calculate", command=calculate_si).pack(pady=10)
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
