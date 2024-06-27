from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

number1 = Entry(root, width=50)
number2 = Entry(root, width=50)
number1.pack()
number2.pack()

result_label = Label(root, text="Result: " + str(0))
result_label.pack()

def add():
    try:
        number1_value = int(number1.get())
        number2_value = int(number2.get())
        result = number1_value + number2_value
        result_label.config(text="Result: " + str(result))
        messagebox.showinfo("Result: ", "The result is: " +str(result))
    except ValueError as e:
        messagebox.showerror("Error", "Invalid Input")
        result_label.config(text="Result: " + "Invalid input")

def reset():
    result_label.config(text="Result: " + str(0))
    number1.delete(0, END)
    number2.delete(0, END)

add_button = Button(root, width=50, text="Add", command=add)
add_button.pack()

reset_button = Button(root, width=30, text="Reset", command=reset, bg="red", fg="white")
reset_button.pack()

root.mainloop()
