import tkinter as tk

LIGHT_GRAY = "#f5f5f5"
LABEL_COLOR = "#25265E"
LIGHT_SKYB = "#CCEDFF"
WHITE = "#FFFFFF"
OFF_WHITE = "#E7F508"
LIGHT_BLUE = "#2DD604"
REDD = "#E12120"

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)


class Calculate:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x660")
        self.window.resizable(0, 0)
        self.window.title("DSC-NUST Calculator")

        # display expressions
        self.total_solution = ""
        self.current_solution = ""

        # displaying the display and buttons frames
        ## display frame
        self.display_frame = self.create_display_frame()
        ### display value labels
        self.total_label, self.label = self.create_display_labels()
        ## display buttons
        ### **Digits dictionary
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 3)
        }
        ### ***Calculating Operations dictionary
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_solution, anchor=tk.E, bg=LIGHT_SKYB,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_solution, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR,
                         padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_solution += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE,
                               borderwidth=0,
                               command=lambda x=digit: self.add_to_expression(x))  # convert int=digit to string=digit
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_solution += operator
        self.total_solution += self.current_solution
        self.current_solution = ""
        self.update_total_label()
        self.update_label()

    ## operations method
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_solution = ""
        self.total_solution = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=REDD, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0,
                           command=self.clear)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_solution += self.current_solution
        self.update_total_label()
        
        # Handle calculation errors
        try:
            self.current_solution = str(eval(self.total_solution))

            self.total_solution = ""
        except Exception as e:
            self.current_solution = "Invalid"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=4, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        self.total_label.config(text=self.total_solution)

    def update_label(self):
        self.label.config(text=self.current_solution[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculate()
    calc.run()