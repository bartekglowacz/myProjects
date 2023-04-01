import re
import tkinter as tk

import matplotlib.pyplot as draw


def formula_converter(formula):
    formula = formula.replace('ctg', 'cot')
    formula = formula.replace('^', '**')

    formula = re.sub('sin', 'math.sin', formula)
    formula = re.sub('cos', 'math.cos', formula)
    formula = re.sub('tg', 'math.tan', formula)
    formula = re.sub('cot', '1/math.tan', formula)
    formula = re.sub('sqrt', 'math.sqrt', formula)
    return formula


def drawing_function():
    formula_input = formula_input_field.get()
    formula_input = formula_input.lower()
    formula_input = formula_converter(formula_input)

    x_value, y_value = [], []
    x = 0
    while x < 1:
        try:
            y = eval(formula_input)
            x_value.append(x)
            y_value.append(y)
            draw.plot(x_value, y_value, color="blue")
            draw.autoscale()
            draw.pause(0.1)
            x = x + 0.1
        except Exception as e:
            print(f"{e}")
            x = x + 0.1
            continue

    print(x_value)
    print(y_value)
    return [x_value, y_value]


def print_data():
    x_value = drawing_function()[0]
    y_value = drawing_function()[1]
    print(f"W funkcji print_data:\n{x_value = }\n{y_value = }")
    return [x_value, y_value]


# tworzenie okna
root = tk.Tk()
root.title("Rysowanie wykresu funkcji")

# tworzenie pola tekstowego do wprowadzania wzoru funkcji
formula_input_field = tk.Entry(root, width=30)
formula_input_field.pack(pady=10)

# tworzenie przycisku do rysowania wykresu
plot_button = tk.Button(root, text="Rysuj wykres", command=drawing_function)
plot_button.pack(pady=10)

# wywołanie metody mainloop(), która umożliwia wyświetlanie okna i interakcję z użytkownikiem
root.mainloop()
