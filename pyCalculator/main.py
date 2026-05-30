import tkinter as tk

class PyCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("pyCalculator")
        self.root.geometry("320x450")
        self.root.resizable(0, 0)
        self.root.configure(bg="#141414")

        self.expression = ""
        self.display_var = tk.StringVar()

        self.create_ui()
        self.bind_keys()

    def create_ui(self):
        # the display
        display_frame = tk.Frame(self.root, bg="#213720")
        display_frame.pack(expand=True, fill="both", pady=10)

        display_label = tk.Label(display_frame, textvariable=self.display_var, anchor="e", bg="#202020", fg="white", font=("Arial", 32, "bold"), padx=20)
        display_label.pack(expand=True, fill="both")

        # buttons
        buttons_frame = tk.Frame(self.root, bg="#202020")
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            ('C', "#ca2e2e"), ('(', '#4d4d4d'), (')', '#4d4d4d'), ('/', '#ff9933'),
            ('7', '#333333'), ('8', '#333333'), ('9', '#333333'), ('*', '#ff9933'),
            ('4', '#333333'), ('5', '#333333'), ('6', '#333333'), ('-', '#ff9933'),
            ('1', '#333333'), ('2', '#333333'), ('3', '#333333'), ('+', '#ff9933'),
            ('0', '#333333'), ('.', '#333333'), ('=', '#ff9933')
        ]

        row_val, col_val = 0, 0
        for text, color in buttons:
            btn = tk.Button(buttons_frame, text=text, font=("Arial", 18), bg=color, fg="white", bd=0, command=lambda t=text: self.on_button_click(t))
            

            if text == '0':
                btn.grid(row=row_val, column=col_val, columnspan=2, sticky="nsew", padx=2, pady=2)
                col_val += 2
            elif text == '=':
                btn.grid(row=row_val, column=col_val, columnspan=2, sticky="nsew", padx=2, pady=2)
                col_val += 2
            else:
                btn.grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
                col_val += 1
            
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            self.evaluate_expression()      # evaluate using library function
        else:
            self.expression += str(char)    # keyboard input / button click
        self.update_display()

    def evaluate_expression(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except ZeroDivisionError:
            self.expression = "Error"
        except Exception:
            self.expression = "Error"

    def update_display(self):
        self.display_var.set(self.expression)

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.on_button_click('='))
        self.root.bind("<BackSpace>", self.handle_backspace)
        self.root.bind("<Key>", self.handle_keypress)

    def handle_backspace(self, event):
        self.expression = self.expression[:-1]
        self.update_display()

    def handle_keypress(self, event):
        valid_chars = "0123456789+-*/()."
        if event.char in valid_chars:
            self.on_button_click(event.char)

if __name__=="__main__":
    root=tk.Tk()
    app=PyCalculator(root)
    root.mainloop()