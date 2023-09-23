<<<<<<< HEAD
from tkinter import *


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        undo_stack = []
        num = StringVar()  # создадим переменную для отображения значений на табло калькулятора
        num.set(0)  # установим значение переменной равное 0
        self.label = Entry(text=num, justify=RIGHT)
        self.label.pack()

        Button(text=1).place(x=0, y=50)
        Button(text=2).place(x=75, y=50)
        Button(text=3).place(x=150, y=50)
        Button(text=4).place(x=230, y=50)
        Button(text=5).place(x=310, y=50)
        Button(text=6).place(x=0, y=75)
        Button(text=7).place(x=75, y=75)
        Button(text=8).place(x=150, y=75)
        Button(text=9).place(x=230, y=75)
        Button(text=0).place(x=310, y=75)
        Button(text="/").place(x=0, y=100)
        Button(text="*").place(x=75, y=100)
        Button(text="-").place(x=150, y=100)
        Button(text="+").place(x=230, y=100)
        Button(text="=").place(x=310, y=100)

    def on_button_click(self, value):
        pass
    
def main():
    root = Tk()
    root.title("")
    root.geometry("300x300")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()

# from tkinter import *
# from tkinter import ttk
#
# class Example(Frame):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         display = Entry(width=20, font=("Arial", 20))
#         display.grid(row=0, column=0, columnspan=4)
#
#         style = ttk.Style()
#         style.configure("TButton", padding=10, font=("Arial", 16))
#
#         buttons = [
#             '7', '8', '9', '/',
#             '4', '5', '6', '*',
#             '1', '2', '3', '-',
#             '0', 'C', '+', '='
#         ]
#
#         row_val = 1
#         col_val = 0
#
#         undo_stack = []
#
#         def on_button_click(value):
#             current_text = display.get()
#             if value == "=":
#                 try:
#                     result = eval(current_text)
#                     display.delete(0, END)
#                     display.insert(END, str(result))
#                 except:
#                     display.delete(0, END)
#                     display.insert(END, "Ошибка")
#             elif value == "C":
#                 display.delete(0, END)
#             elif value == "Undo":
#                 if undo_stack:
#                     last_action = undo_stack.pop()
#                     display.delete(0, END)
#                     display.insert(END, last_action)
#             else:
#                 display.insert(END, value)
#                 undo_stack.append(current_text)
#
#         for button in buttons:
#             Button(text=button, width=5, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
#             col_val += 1
#             if col_val > 3:
#                 col_val = 0
#                 row_val += 1
#
#         Button(text="Undo", width=5, command=lambda: on_button_click("Undo")).grid(row=row_val, column=col_val)
#
# def main():
#     root = Tk()
#     root.title("Калькулятор")
#     app = Example()
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()
=======
from tkinter import *


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        num = StringVar()  # создадим переменную для отображения значений на табло калькулятора
        num.set(0)  # установим значение переменной равное 0
        label = Entry(text=num, justify=RIGHT)
        label.pack()

        Button(text=1).place(x=0, y=50)
        Button(text=2).place(x=75, y=50)
        Button(text=3).place(x=150, y=50)
        Button(text=4).place(x=230, y=50)
        Button(text=5).place(x=310, y=50)
        Button(text=6).place(x=0, y=75)
        Button(text=7).place(x=75, y=75)
        Button(text=8).place(x=150, y=75)
        Button(text=9).place(x=230, y=75)
        Button(text=0).place(x=310, y=75)
        Button(text="/").place(x=0, y=100)
        Button(text="*").place(x=75, y=100)
        Button(text="-").place(x=150, y=100)
        Button(text="+").place(x=230, y=100)
        Button(text="=").place(x=310, y=100)

def main():
    root = Tk()
    root.title("")
    root.geometry("300x300")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()
>>>>>>> 31327bb95111b94509d71d6f998f342e3dd10eeb
