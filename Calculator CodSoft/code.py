from tkinter import *
from tkinter.ttk import Combobox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error (Divide by 0)"
        else:
            result = "Invalid"

        result_label.config(text="Result: " + str(result))

    except:
        result_label.config(text="Invalid Input")

# Create window
window = Tk()
window.title("Simple Calculator")
window.geometry("500x300")

# Input fields
label1 = Label(window, text="Enter first number:", font = ("Arial", 9))
label1.pack()
entry1 = Entry(window)
entry1.pack()

label2 = Label(window, text="Enter second number:", font = ("Arial", 9))
label2.pack()
entry2 = Entry(window)
entry2.pack()

# Operation selection
label3 = Label(window, text="Choose operation:", font = ("Arial", 9))
label3.pack()

operation = StringVar()
operation.set("+")  # default

combo = Combobox(window, textvariable = operation, values = ["+", "-", "*", "/"])
combo.pack()
# Calculate button
button = Button(window, text="Calculate", command=calculate, font = ("Arial", 9)).pack(pady=10)

# Result label
result_label = Label(window, text="Result: ", font = ("Arial", 11))
result_label.pack()

# Run app
window.mainloop()