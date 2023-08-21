import tkinter as tk

def evaluate_expression():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def append_to_expression(char):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_expression + char)

def clear_entry():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Helvetica", 16), bd=10, justify="right")
entry.grid(row=0, column=0, columnspan=4)

button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_val = 1
col_val = 0

for text in button_texts:
    tk.Button(
        root, 
        text=text, 
        font=("Helvetica", 16),
        command=lambda t=text: append_to_expression(t) if t != "=" else evaluate_expression() 
    ).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_button = tk.Button(root, text="C", font=("Helvetica", 16), command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=4)

root.mainloop()
