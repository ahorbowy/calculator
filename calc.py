from tkinter import *

# Inicjalizacja zmiennych globalnych
expression = ""
result = 0

# Funkcja obsługująca kliknięcie przycisku


def clicked(button):
    global expression
    expression += str(button)
    result_label.config(text=expression)

# Funkcja obsługująca przycisk "="


def equals():
    global result, expression
    result = eval(expression)
    expression = str(result)
    result_label.config(text=result)

# Funkcja obsługująca przycisk "AC"


def operation_AC():
    global expression, result
    result = 0
    expression = ""
    result_label.config(text=result)

# Funkcja obsługująca przycisk "+/-"


def negative():
    global result, expression
    if expression != "":
        temp = int(expression)
        if temp > 0:
            temp = -temp
            expression = str(temp)
        elif temp <= 0:
            temp = abs(temp)
            expression = str(temp)
        result_label.config(text=temp)
    else:
        if result > 0:
            result = -result
        elif result <= 0:
            result = abs(result)
        result_label.config(text=result)

# Funkcja obsługująca przycisk "%"


def percent():
    global result, expression
    if expression != "":
        temp = int(float(expression))
        expression = str(temp / 100)
        result_label.config(text=expression)
    else:
        result = str(result / 100)
        result_label.config(text=result)

# Funkcje obsługujące zmianę koloru przycisków przy najechaniu myszką


def on_enter_1_9(event):
    event.widget.config(bg="#1E7E0E")


def on_leave_1_9(event):
    event.widget.config(bg="#5CD049")


def on_enter_actions(event):
    event.widget.config(bg="#5CD049")


def on_leave_actions(event):
    event.widget.config(bg="#1E7E0E")


def on_enter_equals(event):
    event.widget.config(bg="#D19000")


def on_leave_equals(event):
    event.widget.config(bg="#E7A107")


# Główne okno tkinter
if __name__ == "__main__":
    calc = Tk()
    calc.title("Calculator")  # Nazwa okna
    calc.geometry("330x400")  # Rozmiar okna
    calc.configure(bg="#332F2E")  # Kolor tła
    # Blokada zmiany rozmiaru oraz maksymalizowania okienka
    calc.resizable(False, False)
    font_for_buttons = ('Times', 10, 'bold')

    # Tworzenie przycisków i ich rozmieszczenie
    button_0 = Button(calc, bg="#5CD049", activebackground="#1E7E0E", text="0",
                      width="18", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked(0))
    button_0.place(x=20, y=340)
    button_0.bind('<Enter>', on_enter_1_9)
    button_0.bind('<Leave>', on_leave_1_9)

    button_dot = Button(calc, bg="#5CD049", activebackground="#1E7E0E",
                        text=".", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked('.'))
    button_dot.place(x=175, y=340)
    button_dot.bind('<Enter>', on_enter_1_9)
    button_dot.bind('<Leave>', on_leave_1_9)

    button_equals = Button(calc, bg="#E7A107", activebackground="#AB7600",
                           text="=", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: equals())
    button_equals.place(x=255, y=340)
    button_equals.bind('<Enter>', on_enter_equals)
    button_equals.bind('<Leave>', on_leave_equals)

    button_1 = Button(calc, bg="#5CD049", activebackground="#1E7E0E",
                      text="1", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked(1))
    button_1.place(x=20, y=280)
    button_1.bind('<Enter>', on_enter_1_9)
    button_1.bind('<Leave>', on_leave_1_9)

    button_2 = Button(calc, bg="#5CD049", activebackground="#1E7E0E",
                      text="2", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked(2))
    button_2.place(x=97, y=280)
    button_2.bind('<Enter>', on_enter_1_9)
    button_2.bind('<Leave>', on_leave_1_9)

    button_3 = Button(calc, bg="#5CD049", activebackground="#1E7E0E",
                      text="3", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked(3))
    button_3.place(x=175, y=280)
    button_3.bind('<Enter>', on_enter_1_9)
    button_3.bind('<Leave>', on_leave_1_9)

    button_plus = Button(
        calc, bg="#1E7E0E", activebackground="#1E7E0E", text="+", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked('+'))
    button_plus.place(x=255, y=280)
    button_plus.bind('<Enter>', on_enter_actions)
    button_plus.bind('<Leave>', on_leave_actions)

    button_4 = Button(calc, bg="#5CD049", activebackground="#1E7E0E",
                      text="4", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked(4))
    button_4.place(x=20, y=220)
    button_4.bind('<Enter>', on_enter_1_9)
    button_4.bind('<Leave>', on_leave_1_9)

    button_5 = Button(calc, bg="#5CD049", activebackground="#1E7E0E",
                      text="5", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked(5))
    button_5.place(x=97, y=220)
    button_5.bind('<Enter>', on_enter_1_9)
    button_5.bind('<Leave>', on_leave_1_9)

    button_6 = Button(calc, bg="#5CD049", activebackground="#1E7E0E",
                      text="6", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked(6))
    button_6.place(x=175, y=220)
    button_6.bind('<Enter>', on_enter_1_9)
    button_6.bind('<Leave>', on_leave_1_9)

    button_minus = Button(calc, bg="#1E7E0E", activebackground="#1E7E0E", text="-",
                          width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked('-'))
    button_minus.place(x=255, y=220)
    button_minus.bind('<Enter>', on_enter_actions)
    button_minus.bind('<Leave>', on_leave_actions)

    button_7 = Button(calc, bg="#5CD049", activebackground="#1E7E0E", text="7",
                      width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked(7))
    button_7.place(x=20, y=160)
    button_7.bind('<Enter>', on_enter_1_9)
    button_7.bind('<Leave>', on_leave_1_9)

    button_8 = Button(calc, bg="#5CD049", activebackground="#1E7E0E",
                      text="8", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked(8))
    button_8.place(x=97, y=160)
    button_8.bind('<Enter>', on_enter_1_9)
    button_8.bind('<Leave>', on_leave_1_9)

    button_9 = Button(calc, bg="#5CD049", activebackground="#1E7E0E",
                      text="9", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked(9))
    button_9.place(x=175, y=160)
    button_9.bind('<Enter>', on_enter_1_9)
    button_9.bind('<Leave>', on_leave_1_9)

    button_x = Button(calc, bg="#1E7E0E", activebackground="#1E7E0E",
                      text="x", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked('*'))
    button_x.place(x=255, y=160)
    button_x.bind('<Enter>', on_enter_actions)
    button_x.bind('<Leave>', on_leave_actions)

    button_AC = Button(calc, bg="#1E7E0E", activebackground="#1E7E0E",
                       text="AC", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: operation_AC())
    button_AC.place(x=20, y=100)
    button_AC.bind('<Enter>', on_enter_actions)
    button_AC.bind('<Leave>', on_leave_actions)

    button_plus_minus = Button(
        calc, bg="#1E7E0E", activebackground="#1E7E0E", text="+/-", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: negative())
    button_plus_minus.place(x=97, y=100)
    button_plus_minus.bind('<Enter>', on_enter_actions)
    button_plus_minus.bind('<Leave>', on_leave_actions)

    button_percent = Button(
        calc, bg="#1E7E0E", activebackground="#1E7E0E", text="%", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: percent())
    button_percent.place(x=175, y=100)
    button_percent.bind('<Enter>', on_enter_actions)
    button_percent.bind('<Leave>', on_leave_actions)

    button_divide = Button(
        calc, bg="#1E7E0E", activebackground="#1E7E0E", text="÷", width="7", height="2", font=font_for_buttons, relief="solid", bd="1", command=lambda: clicked('/'))
    button_divide.place(x=255, y=100)
    button_divide.bind('<Enter>', on_enter_actions)
    button_divide.bind('<Leave>', on_leave_actions)

    # Label wyświetlający wynik
    result_label = Label(calc, text=result, width="11",
                         height="1", font=('Times', 35))
    result_label.place(x=20, y=20)
    result_label.configure(bg="#332F2E", anchor=E, fg="white")

    calc.mainloop()
