import tkinter as tk
from tkinter import ttk
from calculator import Add, Subtract, Multiply, Divide
from list_operations import sum_list, product_list, average_list
from concurrent_operations import execute_operations
from decorators import log_operation, operation_history

def validate_operands():
    """Validate operands and return them along with a validity flag.

    Returns:
        operand1 (float): The first operand.
        operand2 (float): The second operand.
        is_valid (bool): A flag indicating whether the operands are valid.
    """
    operand1 = operand1_entry.get().strip()
    operand2 = operand2_entry.get().strip()
    
    if not operand1 or not operand2:
        result_label.config(text="Both operands are required.")
        return None, None, False

    try:
        operand1 = float(operand1)
        operand2 = float(operand2)
    except ValueError:
        result_label.config(text="Invalid input.")
        return None, None, False
    
    return operand1, operand2, True


def perform_and_show(op_class):
    """Perform the operation represented by op_class and display the result.

    Args:
        op_class (class): A class representing the operation to be performed.
    """
    operand1, operand2, is_valid = validate_operands()
    if not is_valid:
        return

    op = op_class(operand1, operand2)
    op.perform_operation()
    result_label.config(text=op.display_result())
    log_operation(op.perform_operation)


def perform_list_operations():
    """Perform sum, product, and average operations on a list of numbers."""
    raw_numbers = list_entry.get().split(',')
    filtered_numbers = filter(lambda x: x.strip() != "", raw_numbers)
    
    try:
        numbers = list(map(float, filtered_numbers))
        if not numbers:
            list_result_label.config(text="No numbers provided.")
            return

        sum_result = sum_list(numbers)
        product_result = product_list(numbers)
        average_result = average_list(numbers)
        list_result_label.config(text=f"Sum: {sum_result}, Product: {product_result}, Avg: {average_result}")
    except ValueError:
        list_result_label.config(text="Invalid input.")


def perform_parallel_operations():
    """Perform addition, subtraction, multiplication, and division in parallel."""
    operand1 = operand1_entry.get().strip()
    operand2 = operand2_entry.get().strip()

    if not operand1 or not operand2:
        parallel_result_label.config(text="Both operands are required.")
        return

    try:
        op1 = Add(float(operand1), float(operand2))
        op2 = Subtract(float(operand1), float(operand2))
        op3 = Multiply(float(operand1), float(operand2))
        op4 = Divide(float(operand1), float(operand2))
    except ValueError:
        parallel_result_label.config(text="Invalid input.")
        return

    results = execute_operations([op1, op2, op3, op4])
    parallel_result_label.config(text=f"Results: {results}")


def show_history():
    """Display the history of operations in a Tkinter Text widget."""
    history_text.delete(1.0, tk.END)
    for item in operation_history:
        history_text.insert(tk.END, f"{item}\n")


def check_and_perform_divide():
    """Validate operands and perform division if they are non-zero."""
    operand1, operand2, is_valid = validate_operands()
    if not is_valid:
        return

    if operand1 == 0 or operand2 == 0:
        result_label.config(text="One or both operands are zero.")
        return
    
    perform_and_show(Divide)


# Initialize GUI
root = tk.Tk()
root.title("Advanced Calculator")
root.resizable(False, False)
# Label and Button for parallel operations
parallel_result_label = ttk.Label(root, text="Parallel Results:")
parallel_result_label.grid(column=0, row=7, columnspan=2)
parallel_button = ttk.Button(root, text="Run Parallel", command=perform_parallel_operations)
parallel_button.grid(column=0, row=8, columnspan=2)

# Text widget to display history
history_text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
history_text.grid(column=0, row=9, columnspan=2)

# Button to show history
history_button = ttk.Button(root, text="Show History", command=show_history)
history_button.grid(column=0, row=10, columnspan=2)
# Entry widgets for operands
operand1_entry = ttk.Entry(root, width=15)
operand1_entry.grid(column=0, row=0)
operand2_entry = ttk.Entry(root, width=15)
operand2_entry.grid(column=1, row=0)

# Entry widget for list operations
list_entry = ttk.Entry(root, width=30)
list_entry.grid(column=0, row=4, columnspan=2)

# Label to show result
result_label = ttk.Label(root, text="Result:")
result_label.grid(column=0, row=1, columnspan=2)

# Label to show list operations result
list_result_label = ttk.Label(root, text="List Result:")
list_result_label.grid(column=0, row=5, columnspan=2)

# Buttons for operations
add_button = ttk.Button(root, text="Add", command=lambda: perform_and_show(Add))

add_button.grid(column=0, row=2)

subtract_button = ttk.Button(root, text="Subtract", command=lambda: perform_and_show(Subtract))
subtract_button.grid(column=1, row=2)

multiply_button = ttk.Button(root, text="Multiply", command=lambda: perform_and_show(Multiply))
multiply_button.grid(column=0, row=3)

divide_button = ttk.Button(root, text="Divide", command=check_and_perform_divide)
divide_button.grid(column=1, row=3)

# Button for list operations
list_button = ttk.Button(root, text="List Operations", command=perform_list_operations)
list_button.grid(column=0, row=6, columnspan=2)

if __name__ == "__main__":
    # Run the GUI
    root.mainloop()
