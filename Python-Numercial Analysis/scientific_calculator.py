# This program implements Scientific Calculator
from tkinter import *
from tkinter import messagebox
import math
from time import strftime

# Main Screen
root = Tk()
root.geometry('325x400')
root['bg'] = "#212121"
root.title("Calculator")
root.resizable(False, False)
root.grid()
# Create entry
data = StringVar()
label = Entry(root, font=('arial', 20, 'bold'), bg="gray1", fg='white', bd=20, width=22, justify="right")
label.grid(row=0, column=0, columnspan=4, pady=1)


def press(num):
    val = len(label.get())
    label.insert(val, num)


def key_press():
    if label.get() == '0':
        label.delete(0, END)


def clear():  # Clear button
    display = str(label.get())
    if display == '':
        label.insert(0, '')
    else:
        label.delete(0, END)
        label.insert(0, '')


def backspace():  # Backspace button
    val = len(label.get())
    display = str(label.get())
    if display == '0':
        label.delete(0, END)
        label.insert(0, '')
    else:
        label.delete(0, END)
        label.insert(0, display[0: val-1])


def equal():
    try:  # Get and compute the "ans" value
        ans = label.get()
        result = eval(ans)
        label.delete(0, END)  # Clear the typo from the screen
        label.insert(0, str(result))  # Show the result
    except SyntaxError as s:
        messagebox.showerror("Syntax Error", str(s))
    except ZeroDivisionError as z:
        messagebox.showerror("Math Error",  str(z))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def maths_pm():
    try:
        ans = float(label.get())
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def decimal_p():
    try:
        ans = float(label.get())
        ans = ('%.3f' % ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def math_standard(op):
    val = len(label.get())
    label.insert(val, op)


def fraction():  # Calculate fraction
    try:
        ans = float(label.get())
        ans = 1/ans
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def pow_xy():  # Power X of Y
    val = len(label.get())
    label.insert(val, '**')


def pow2():  # X Power by 2
    try:
        ans = float(label.get())
        ans = ans ** 2
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def pow10():  # 10 power by X
    try:
        ans = float(label.get())
        ans = 10 ** ans
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def pow2x():  # 2 power by X
    try:
        ans = float(label.get())
        ans = 2 ** ans
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def percent():  # Percentage %
    try:
        ans = float(label.get())
        ans = ans / 100
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def sqrt3():  # Square Root 3
    try:
        ans = float(label.get())
        ans = ans ** (1/3)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def double_e():  # (10^n) * n
    try:
        ans = float(label.get())
        ans = 10 ** ans * ans
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def exp():  # Exponentiation
    val = len(label.get())
    label.insert(val, '* 10 **')


def pi():  # Pi value
    ans = str(label.get())
    if ans == '':  # Empty space
        label.insert(0, str(math.pi))
    else:
        ans = float(label.get())
        ans = math.pi * ans
        label.delete(0, END)
        label.insert(0, str(ans))


def euler():  # Euler ** n
    ans = str(label.get())
    if ans == '':
        label.insert(0, str(math.e))
    else:
        ans = float(label.get())
        ans = math.e ** ans
        label.delete(0, END)
        label.insert(0, str(ans))


def tau_pi():  # 2 * pi
    ans = str(label.get())
    if ans == '':
        label.insert(0, str(math.tau))
    else:
        ans = float(label.get())
        ans = math.tau * ans
        label.delete(0, END)
        label.insert(0, str(ans))


def rad():  # Radians
    try:
        ans = float(label.get())
        ans = math.radians(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def deg():  # Degrees
    try:
        ans = float(label.get())
        ans = math.degrees(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def sin():  # Sin in radians
    try:
        ans = float(label.get())
        ans = math.sin(math.radians(ans))
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def cos():  # Cos in radians
    try:
        ans = float(label.get())
        ans = math.cos(math.radians(ans))
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def tan():  # Tan in radians
    try:
        ans = float(label.get())
        ans = math.tan(math.radians(ans))
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def arc_sin():  # Arc_sin
    try:
        ans = float(label.get())
        ans = math.asin(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def arc_cos():  # Arc_cos
    try:
        ans = float(label.get())
        ans = math.acos(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def arc_tan():  # Arc_tan
    try:
        ans = float(label.get())
        ans = math.atan(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def sin_h():  # Sin_h
    try:
        ans = float(label.get())
        ans = math.sinh(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def cos_h():  # Cos_h
    try:
        ans = float(label.get())
        ans = math.cosh(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def tan_h():  # Tan_h
    try:
        ans = float(label.get())
        ans = math.tanh(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def log():  # Logarithm base X
    try:
        ans = float(label.get())
        ans = math.log(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def log2():  # Logarithm base 2
    try:
        ans = float(label.get())
        ans = math.log2(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def log10():  # Logarithm base 10
    try:
        ans = float(label.get())
        ans = math.log10(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def math_ceil():  # Round the number up to the nearest integer
    try:
        ans = float(label.get())
        ans = math.ceil(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def math_floor():  # Round the number down to the nearest integer
    try:
        ans = float(label.get())
        ans = math.floor(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def sqrt():  # Square Root
    try:
        ans = float(label.get())
        ans = math.sqrt(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


def factorial():  # Factorial
    try:
        ans = int(label.get())
        ans = math.factorial(ans)
        label.delete(0, END)
        label.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Value Error", str(e))


# Create the buttons and their functions
label.bind("<Return>", equal)
label.bind("<Escape>", clear)
label.bind("<Key-1>", key_press())
label.bind("<Key-2>", key_press())
label.bind("<Key-3>", key_press())
label.bind("<Key-4>", key_press())
label.bind("<Key-5>", key_press())
label.bind("<Key-6>", key_press())
label.bind("<Key-7>", key_press())
label.bind("<Key-8>", key_press())
label.bind("<Key-9>", key_press())
label.bind("<Key-.>", key_press())
label.focus_set()
label.insert(0, '')


# Calculator buttons (for macOS you change the fg of some buttons to red)
# Row 1
btn_percent = Button(root, text="%", width=6, height=2, font=('arial', 12, 'bold'),
                     bd=4, bg="#d4d4d2", fg="black", command=percent, activebackground="#b3b3b3")
btn_percent.grid(row=1, column=0, pady=1)
btn_pm = Button(root, text=chr(177), width=6, height=2, font=('arial', 12, 'bold'),
                bd=4, bg="#d4d4d2", fg="black", command=maths_pm)
btn_pm.grid(row=1, column=1, pady=1)
btn_clearall = Button(root, text="AC", width=6, height=2, font=('arial', 12, 'bold'),
                      bd=4, bg="#d4d4d2", fg="red", command=clear)
btn_clearall.grid(row=1, column=2, pady=1)
btn_del = Button(root, text="\u232B", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#d4d4d2", fg="red", command=backspace)
btn_del.grid(row=1, column=3, pady=1)
btn_npi = Button(root, text="π", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=pi)
btn_npi.grid(row=1, column=4, pady=1)
btn_eu = Button(root, text="e", width=6, height=2, font=('arial', 12, 'bold'),
                bd=4, bg="#212121", fg="black", command=euler)
btn_eu.grid(row=1, column=5, pady=1)
btn_tau = Button(root, text="2π", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=tau_pi)
btn_tau.grid(row=1, column=6, pady=1)
btn_double_eu = Button(root, text="2e", width=6, height=2, font=('arial', 12, 'bold'),
                       bd=4, bg="#212121", fg="black", command=double_e)
btn_double_eu.grid(row=1, column=7, pady=1)
btn_exp = Button(root, text="exp", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=exp)
btn_exp.grid(row=1, column=8, pady=1)
# Row 2
btn_frac = Button(root, text="\u00b9/\u2093", width=6, height=2, font=('arial', 12, 'bold'),
                  bd=4, bg="#212121", fg="black", command=fraction)
btn_frac.grid(row=2, column=0, pady=1)

btn_sqrt = Button(root, text="\u00b2√", width=6, height=2, font=('arial', 12, 'bold'),
                  bd=4, bg="#212121", fg="black", command=sqrt)
btn_sqrt.grid(row=2, column=1, pady=1)

btn_pow2 = Button(root, text="x\u00b2", width=6, height=2, font=('arial', 12, 'bold'),
                  bd=4, bg="#212121", fg="black", command=pow2)
btn_pow2.grid(row=2, column=2, pady=1)

btn_div = Button(root, text=chr(247), width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#ff9500", fg="black", command=lambda: math_standard("/"))
btn_div.grid(row=2, column=3, pady=1)
btn_brl = Button(root, text="(", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=lambda: press("("))
btn_brl.grid(row=2, column=4, pady=1)
btn_br = Button(root, text=")", width=6, height=2, font=('arial', 12, 'bold'),
                bd=4, bg="#212121", fg="black", command=lambda: press(")"))
btn_br.grid(row=2, column=5, pady=1)
btn_pow_y = Button(root, text="x^y", width=6, height=2, font=('arial', 12, 'bold'),
                   bd=4, bg="#212121", fg="black", command=pow_xy)
btn_pow_y.grid(row=2, column=6, pady=1)
btn_pow_10 = Button(root, text="x^10", width=6, height=2, font=('arial', 12, 'bold'),
                    bd=4, bg="#212121", fg="black", command=pow10)
btn_pow_10.grid(row=2, column=7, pady=1)
btn_2_pow = Button(root, text="2^x", width=6, height=2, font=('arial', 12, 'bold'),
                   bd=4, bg="#212121", fg="black", command=pow2x)
btn_2_pow.grid(row=2, column=8, pady=1)
btn_mul = Button(root, text="x", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#ff9500", fg="black", command=lambda: math_standard("*"))
# Row 3
btn_mul.grid(row=3, column=3, pady=1)
btn_mod = Button(root, text="mod", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=lambda: math_standard("%"))
btn_mod.grid(row=3, column=4, pady=1)
btn_log = Button(root, text="ln", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=log)
btn_log.grid(row=3, column=5, pady=1)
btn_log_10 = Button(root, text="log10", width=6, height=2, font=('arial', 12, 'bold'),
                    bd=4, bg="#212121", fg="black", command=log10)
btn_log_10.grid(row=3, column=6, pady=1)
btn_log_2 = Button(root, text="log2", width=6, height=2, font=('arial', 12, 'bold'),
                   bd=4, bg="#212121", fg="black", command=log2)
btn_log_2.grid(row=3, column=7, pady=1)
btn_factorial = Button(root, text="x!", width=6, height=2, font=('arial', 12, 'bold'),
                       bd=4, bg="#212121", fg="black", command=factorial)
btn_factorial.grid(row=3, column=8, pady=1)
# Row 4
btn_sub = Button(root, text="-", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#ff9500", fg="black", command=lambda: math_standard("-"))
btn_sub.grid(row=4, column=3, pady=1)
btn_ceil = Button(root, text="ceil", width=6, height=2, font=('arial', 12, 'bold'),
                  bd=4, bg="#212121", fg="black", command=math_ceil)
btn_ceil.grid(row=4, column=4, pady=1)
btn_arc_sin = Button(root, text="sin^-1", width=6, height=2, font=('arial', 12, 'bold'),
                     bd=4, bg="#212121", fg="black", command=arc_sin)
btn_arc_sin.grid(row=4, column=5, pady=1)
btn_arc_cos = Button(root, text="cos^-1", width=6, height=2, font=('arial', 12, 'bold'),
                     bd=4, bg="#212121", fg="black", command=arc_cos)
btn_arc_cos.grid(row=4, column=6, pady=1)
btn_arc_tan = Button(root, text="tan^-1", width=6, height=2, font=('arial', 12, 'bold'),
                     bd=4, bg="#212121", fg="black", command=arc_tan)
btn_arc_tan.grid(row=4, column=7, pady=1)
btn_three_sqrt = Button(root, text="3^√", width=6, height=2, font=('arial', 12, 'bold'),
                        bd=4, bg="#212121", fg="black", command=sqrt3)
btn_three_sqrt.grid(row=4, column=8, pady=1)
# Row 5
btn_add = Button(root, text="+", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#ff9500", fg="black", command=lambda: math_standard("+"))
btn_add.grid(row=5, column=3, pady=1)
btn_floor = Button(root, text="floor", width=6, height=2, font=('arial', 12, 'bold'),
                   bd=4, bg="#212121", fg="black", command=math_floor)
btn_floor.grid(row=5, column=4, pady=1)
btn_sin = Button(root, text="sin", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=sin)
btn_sin.grid(row=5, column=5, pady=1)
btn_cos = Button(root, text="cos", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=cos)
btn_cos.grid(row=5, column=6, pady=1)
btn_tan = Button(root, text="tan", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=tan)
btn_tan.grid(row=5, column=7, pady=1)
btn_deg = Button(root, text="deg", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=deg)
btn_deg.grid(row=5, column=8, pady=1)
# Row 6
btn_zero = Button(root, text="0", width=6, height=2, font=('arial', 12, 'bold'),
                  bd=4, bg="black", fg="black", command=lambda: press(0))
btn_zero.grid(row=6, column=0, pady=1)
btn_dot = Button(root, text=".", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#505050", fg="black", command=lambda: press("."))
btn_dot.grid(row=6, column=1, pady=1)
btn_equal = Button(root, text="=", width=6, height=2, font=('arial', 12, 'bold'),
                   bd=4, bg="#ff9500", fg="black", command=equal)
btn_equal.grid(row=6, column=2, pady=1)
btn_decimal_p = Button(root, text="DEC", width=6, height=2, font=('arial', 12, 'bold'),
                       bd=4, bg="#ff9500", fg="black", command=decimal_p)
btn_decimal_p.grid(row=6, column=3, pady=1)
btn_sin_h = Button(root, text="sinh", width=6, height=2, font=('arial', 12, 'bold'),
                   bd=4, bg="#212121", fg="black", command=sin_h)
btn_sin_h.grid(row=6, column=4, pady=1)
btn_cos_h = Button(root, text="cosh", width=6, height=2, font=('arial', 12, 'bold'),
                   bd=4, bg="#212121", fg="black", command=cos_h)
btn_cos_h.grid(row=6, column=5, pady=1)
btn_tan_h = Button(root, text="tanh", width=6, height=2, font=('arial', 12, 'bold'),
                   bd=4, bg="#212121", fg="black", command=cos_h)
btn_tan_h.grid(row=6, column=6, pady=1)
btn_rad = Button(root, text="Rad", width=6, height=2, font=('arial', 12, 'bold'),
                 bd=4, bg="#212121", fg="black", command=rad)
btn_rad.grid(row=6, column=7, pady=1)
# Main number pad from 1 to 9
number_pad = "789456123"
i = 0
btn = []
for j in range(3, 6):
    for k in range(3):
        btn.append(Button(root, width=6, height=2, font=('arial', 12, 'bold'),
                          bg="#505050", fg="black", bd=4, text=number_pad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=number_pad[i]: press(x)
        i += 1


def about():
    about_message = messagebox.showinfo("About", "GUI Calculator by Python")
    return about_message


def stop():
    stop_exit = messagebox.askyesno("Scientific Calculator", "Do you want to exit?")
    if stop_exit == YES:
        root.destroy()
        return


def time():
    string = strftime("%d %B %y [%I:%M:%S %P]")
    lebel.config(text=string)
    lebel.after(1000, time)


lebel = Label(root, font=("Calibri", 8, "bold"),
              bg="#212121", fg="white", justify=CENTER)
lebel.grid(row=7, column=0, columnspan=4)
time()


def standard():
    root.geometry("325x400")
    label.grid(row=0, column=0, columnspan=4, ipadx=1, pady=1)
    label.config(width=22)  # Return the entry to original when in standard
    lebel.grid(row=7, column=0, columnspan=4)


def scientific():  # Scientific mode
    root.geometry("750x400")
    label.grid(row=0, column=1, columnspan=8, ipadx=2, pady=2)
    label.config(width=51)  # Expand the entry
    lebel.grid(row=7, column=2, columnspan=4)


# Main Menu
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Option", menu=file_menu)
menubar.add_command(label="About", command=about)
file_menu.add_command(label="Standard", command=standard)
# Switch to scientific calculator
file_menu.add_command(label="Scientific", command=scientific)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=stop)
# Run the code
root.config(menu=menubar)
root.mainloop()
