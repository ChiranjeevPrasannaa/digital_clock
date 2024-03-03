from tkinter import Tk, Label
from datetime import datetime  # Import datetime module

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="burlywood")

label = Label(window, text="", font=("Arial Black", 78, "bold"), bg="steelblue", fg="white")
label.pack(pady=100)

def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500, clock)

clock()  # Start the clock function

window.mainloop()
