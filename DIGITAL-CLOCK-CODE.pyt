import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("🕒 Digital Clock")
root.geometry("500x250")
root.configure(bg="#0a0a2a") 
heading = tk.Label(
    root,
    text="Digital Clock",
    font=("Poppins", 24, "bold"),
    bg="#0a0a2a",
    fg="#00FFCC"
)
heading.pack(pady=10)

time_label = tk.Label(
    root,
    font=("DS-Digital", 70, "bold"),
    bg="#0a0a2a",
    fg="#39FF14"
)
time_label.pack(pady=5)

date_label = tk.Label(
    root,
    font=("Poppins", 20),
    bg="#0a0a2a",
    fg="#00BFFF"
)
date_label.pack()
def update_time():
    current_time = strftime("%H:%M:%S %p")
    current_date = strftime("%A, %B %d, %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)
update_time()
root.mainloop()
