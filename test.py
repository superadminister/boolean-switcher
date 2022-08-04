

class Switcher:
    import tkinter
    from tkinter.font import Font

    tk = tkinter.Tk()
    condition_button = tkinter.Button()
    condition_label = tkinter.Label()
    state = 'False'

    def __init__(self):
        self.condition_label.config(
            text=self.state,
            foreground='red',
            font=self.Font(family='Dejavu Sans Mono', size=25)
        )
        self.condition_label.place(x=150, y=50)
        self.condition_button.config(
            text='Change!',
            command=self.config_state,
            font=self.Font(family='Dejavu Sans Mono', size=13)
        )
        self.condition_button.place(x=150, y=120, width=100, height=40)
        self.tk.title('Boolean Switcher')
        self.tk.resizable(width=False, height=False)
        self.tk.geometry('400x300')
        self.tk.mainloop()

    def config_state(self):
        if self.state == 'True':
            self.state = 'False'
            self.condition_label.config(
                text=self.state, foreground='red'
            )
        elif self.state == 'False':
            self.state = 'True'
            self.condition_label.config(
                text=self.state, foreground='green'
            )


Switcher()
