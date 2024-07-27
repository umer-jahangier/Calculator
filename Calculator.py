import tkinter as tk
from tkinter import messagebox
import numexpr

class CalculatorApp:
    def __init__(self, root):
        #Initializing the main window of the application
        self.root = root
        self.root.title("Calculator")  
        self.root.geometry("400x450")
        self.root.resizable(1, 1)

        #Variable to hold the input text
        self.input_text = tk.StringVar()

        #Creating the widgets (entry field and buttons)
        self.create_widgets()


    def create_widgets(self):
        #Configuring the grid layout for the root window for responsiveness
        self.root.grid_rowconfigure(0, weight=1)  
        self.root.grid_rowconfigure(1, weight=4)
        self.root.grid_columnconfigure(0, weight=1)

        #Creating the input frame for the entry field
        input_frame = tk.Frame(self.root, bg="white")
        input_frame.grid(row=0, column=0, sticky="nsew")
        #Making input filed responsive
        input_frame.grid_rowconfigure(0, weight=1)
        input_frame.grid_columnconfigure(0, weight=1)

        #Creating the entry field for displaying input and results
        self.input_field = tk.Entry(
            input_frame, 
            textvariable=self.input_text, 
            font=('arial', 20, 'bold'), 
            bd=0, 
            insertwidth=3, 
            width=22, 
            borderwidth=10, 
            relief="sunken"
        )
        self.input_field.grid(row=0, column=0, columnspan=4, ipady=10, sticky="nsew")
        self.input_field.focus()

        #Defining button colors
        button_bg = "#f1f1f1"  
        operator_bg = "#d4d4d4"  
        clear_bg = "#ff6666"  
        equal_bg = "#4caf50" 

        #Creating the frame for the buttons
        btns_frame = tk.Frame(self.root)
        btns_frame.grid(row=1, column=0, sticky="nsew")

        #Defining the buttons with their properties (text, row, column, color, command)
        buttons = [
            ('Clear', 1, 0, clear_bg, self.button_clear),
            ('7', 2, 0, button_bg, lambda: self.button_click('7')),
            ('8', 2, 1, button_bg, lambda: self.button_click('8')),
            ('9', 2, 2, button_bg, lambda: self.button_click('9')),
            ('/', 2, 3, operator_bg, lambda: self.button_click('/')),
            ('4', 3, 0, button_bg, lambda: self.button_click('4')),
            ('5', 3, 1, button_bg, lambda: self.button_click('5')),
            ('6', 3, 2, button_bg, lambda: self.button_click('6')),
            ('*', 3, 3, operator_bg, lambda: self.button_click('*')),
            ('1', 4, 0, button_bg, lambda: self.button_click('1')),
            ('2', 4, 1, button_bg, lambda: self.button_click('2')),
            ('3', 4, 2, button_bg, lambda: self.button_click('3')),
            ('-', 4, 3, operator_bg, lambda: self.button_click('-')),
            ('.', 5, 0, button_bg, lambda: self.button_click('.')),
            ('0', 5, 1, button_bg, lambda: self.button_click('0')),
            ('=', 5, 2, equal_bg, self.button_equal),
            ('+', 5, 3, operator_bg, lambda: self.button_click('+')),
        ]

        #Creating and placing the buttons on the grid
        for (text, row, col, bg, cmd) in buttons:
            btn = tk.Button(
                btns_frame, 
                text=text, 
                fg="black", 
                width=10, 
                height=3, 
                bd=0, 
                bg=bg, 
                cursor="hand2", 
                command=cmd
            )
            if text == 'C':
                btn.grid(row=row, column=col, columnspan=4, padx=1, pady=1, sticky="nsew")
            else:
                btn.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

        #Making the buttons and frame responsive
        for i in range(6):
            btns_frame.grid_rowconfigure(i, weight=1)
            if i < 4:
                btns_frame.grid_columnconfigure(i, weight=1)

    #Function to handle button click for numbers and operators
    def button_click(self, item):  
        self.input_field.insert(tk.END, str(item))
        self.input_field.xview_moveto(1)
        self.input_field.focus()

    #Function to handle clear button click
    def button_clear(self):
        self.input_text.set("")
        self.input_field.focus()

    #Function to safely evaluate the mathematical expression using numexpr
    def safe_eval(self, expression):
        try:
            result = numexpr.evaluate(expression)
            return str(result)
        except:
            return "Error"
        
    #Function to handle equal button click to evaluate the expression
    def button_equal(self):
        
        try:
            result = self.safe_eval(self.input_text.get())
            self.input_text.set(result)
        except:
            messagebox.showerror("Error", "Invalid Input")
        self.input_field.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
