#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from tkinter import messagebox
import math

def calculate(operation):
    try:
        num1 = float(entry1.get())

        if operation in ['+', '-', '*', '/', '%', '^']:
            num2 = float(entry2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        elif operation == '^':
            result = num1 ** num2
        elif operation == '√':
            if num1 < 0:
                raise ValueError("Cannot take square root of negative number")
            result = math.sqrt(num1)
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid number(s).")
    except ZeroDivisionError as zde:
        messagebox.showerror("Error", str(zde))

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result:")

# GUI Setup
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("350x400")
root.configure(bg="white")

tk.Label(root, text="Enter first number:", bg="white").pack(pady=5)
entry1 = tk.Entry(root, font=("Helvetica", 12))
entry1.pack(pady=5)

tk.Label(root, text="Enter second number (if needed):", bg="white").pack(pady=5)
entry2 = tk.Entry(root, font=("Helvetica", 12))
entry2.pack(pady=5)

tk.Label(root, text="Operations:", bg="white").pack(pady=10)

button_frame = tk.Frame(root, bg="white")
button_frame.pack()

# First row
tk.Button(button_frame, text="+", width=5, command=lambda: calculate('+')).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="-", width=5, command=lambda: calculate('-')).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="*", width=5, command=lambda: calculate('*')).grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="/", width=5, command=lambda: calculate('/')).grid(row=0, column=3, padx=5, pady=5)

# Second row
tk.Button(button_frame, text="%", width=5, command=lambda: calculate('%')).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="^", width=5, command=lambda: calculate('^')).grid(row=1, column=1, padx=5, pady=5)
tk.Button(button_frame, text="√", width=5, command=lambda: calculate('√')).grid(row=1, column=2, padx=5, pady=5)
tk.Button(button_frame, text="Clear", width=5, command=clear).grid(row=1, column=3, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="Result:", font=("Helvetica", 14), bg="white", fg="blue")
result_label.pack(pady=20)

root.mainloop()


# In[ ]:




