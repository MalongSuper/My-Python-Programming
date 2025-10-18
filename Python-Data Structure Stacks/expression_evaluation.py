# Write a program to create a expression evaluation calculator
from tkinter import *
import math


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def get_top(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]


def is_valid():
    express_input = express_entry.get()
    operators = ["+", "-", "*", "/", "^", "(", ")"]
    if any(char.isalpha() for char in express_input):
        result_label.config(text="Positive Numbers Only", font=("Helvetica", 12))
        return False
    elif all(char not in operators for char in express_input):
        result_label.config(text="Use Operators: +, -, *, /, ^. Example: (a + b) * c / d",
                            font=("Helvetica", 12))
        return False
    elif express_input.count("(") != express_input.count(")"):
        result_label.config(text="Missing Parentheses",
                            font=("Helvetica", 12))
        return False
    else:
        result_label.config(text="")
        return True


def infix_to_postfix(infix_list):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    stack = Stack()
    postfix = []
    number_buffer = ""

    for entry in infix_list:
        if entry.isdigit():
            number_buffer += entry
        else:
            if number_buffer:
                postfix.append(number_buffer)
                number_buffer = ""
            if entry == "(":
                stack.push(entry)
            elif entry == ")":
                while not stack.is_empty() and stack.get_top() != "(":
                    postfix.append(stack.pop())
                stack.pop()
            elif entry in operators:
                while (not stack.is_empty() and stack.get_top() != "(" and
                       operators.get(stack.get_top(), 0) >= operators.get(entry, 0)):
                    postfix.append(stack.pop())
                stack.push(entry)

    if number_buffer:
        postfix.append(number_buffer)
    while not stack.is_empty():
        postfix.append(stack.pop())

    return postfix


def infix_to_prefix(infix_list):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    stack = Stack()
    prefix = []
    number_buffer = ""

    for entry in reversed(infix_list):
        if entry.isdigit():
            number_buffer += entry
        else:
            if number_buffer:
                prefix.append(number_buffer)
                number_buffer = ""
            if entry == ")":
                stack.push(entry)
            elif entry == "(":
                while not stack.is_empty() and stack.get_top() != ")":
                    prefix.append(stack.pop())
                stack.pop()
            elif entry in operators:
                while (not stack.is_empty() and stack.get_top() != ")" and
                       operators.get(stack.get_top(), 0) > operators.get(entry, 0)):
                    prefix.append(stack.pop())
                stack.push(entry)

    if number_buffer:
        prefix.append(number_buffer)
    while not stack.is_empty():
        prefix.append(stack.pop())

    return reversed(prefix)


def evaluate(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        if number2 == 0:
            raise ValueError("Division by Zero")
        return number1 / number2
    elif operator == "^":
        return math.pow(number1, number2)


def evaluate_postfix(postfix_list):  # Evaluate postfix
    stack = Stack()
    operators = ["+", "-", "*", "/", "^"]

    for entry in postfix_list:
        if entry in operators:
            b = stack.pop()
            a = stack.pop()
            temp = evaluate(a, b, entry)
            stack.push(temp)
        else:
            stack.push(int(entry))
    return stack.get_top()


def evaluate_clicked():
    try:
        if is_valid():
            infix_expression = express_entry.get().replace("^", "**")  # Replace ^ with ** for Python
            infix_expression = list(infix_expression.replace(" ", ""))  # Clean input and create a list
            prefix_expression = infix_to_prefix(infix_expression)
            prefix_express_entry.config(state="normal")
            prefix_express_entry.delete(0, END)
            prefix_express_entry.insert(0, " ".join(prefix_expression))
            prefix_express_entry.config(state="readonly")
            postfix_expression = infix_to_postfix(infix_expression)
            postfix_express_entry.config(state="normal")
            postfix_express_entry.delete(0, END)
            postfix_express_entry.insert(0, " ".join(postfix_expression))
            postfix_express_entry.config(state="readonly")
            result = evaluate_postfix(postfix_expression)
            eval_result_entry.config(state="normal")
            eval_result_entry.delete(0, END)
            eval_result_entry.insert(0, result)
            eval_result_entry.config(state="readonly")
    except ValueError as invalid_input:
        result_label.config(text=str(invalid_input), font=("Helvetica", 12))


def clear_clicked():
    express_entry.delete(0, END)
    prefix_express_entry.config(state="normal")
    prefix_express_entry.delete(0, END)
    prefix_express_entry.config(state="readonly")
    postfix_express_entry.config(state="normal")
    postfix_express_entry.delete(0, END)
    postfix_express_entry.config(state="readonly")
    eval_result_entry.config(state="normal")
    eval_result_entry.delete(0, END)
    eval_result_entry.config(state="readonly")
    result_label.config(text="")


# Create GUI
root = Tk()
root.title("Expression Evaluation")
root.geometry("500x500")
root['bg'] = "dark grey"
frame = Frame(root)
frame["bg"] = "dark grey"
frame.place(relx=0.5, rely=0.3, anchor="center")

express_label = Label(frame, text="Expression", bg="dark grey", fg="white")
express_label.grid(row=1, column=2, padx=10, pady=10)
express_entry = Entry(frame, bg="white", fg="black", highlightbackground="black")
express_entry.grid(row=1, column=3, padx=10, pady=10)

prefix_express_label = Label(frame, text="Prefix Expression", bg="dark grey", fg="white")
prefix_express_label.grid(row=3, column=2, padx=10, pady=10)
prefix_express_entry = Entry(frame, bg="white", fg="white", highlightbackground="grey", state="readonly")
prefix_express_entry.grid(row=3, column=3, padx=10, pady=10)

postfix_express_label = Label(frame, text="Postfix Expression", bg="dark grey", fg="white")
postfix_express_label.grid(row=4, column=2, padx=10, pady=10)
postfix_express_entry = Entry(frame, bg="white", fg="white", highlightbackground="grey", state="readonly")
postfix_express_entry.grid(row=4, column=3, padx=10, pady=10)

eval_result_label = Label(frame, text="Evaluated Result", bg="dark grey", fg="white")
eval_result_label.grid(row=5, column=2, padx=10, pady=10)
eval_result_entry = Entry(frame, bg="white", fg="white", highlightbackground="grey", state="readonly")
eval_result_entry.grid(row=5, column=3, padx=10, pady=10)

clear_but = Button(frame, text="Clear", command=clear_clicked, highlightbackground="dark grey")
clear_but.grid(row=6, column=2, padx=2, pady=2, sticky="ew")
eval_but = Button(frame, text="Evaluate", command=evaluate_clicked, highlightbackground="dark grey")
eval_but.grid(row=6, column=3, padx=2, pady=2, sticky="ew")

result_label = Label(frame, text="", bg='dark grey', fg='red')
result_label.grid(row=2, column=2, columnspan=2)

root.mainloop()
