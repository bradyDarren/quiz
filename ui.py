from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface: 

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady= 20, bg=THEME_COLOR)


        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.question = self.canvas.create_text(150, 125, text="Question",font=('Ariel',20, 'italic'), fill='black')
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.score = Label(text="ABC", bg=THEME_COLOR, pady=20)
        self.score.grid(column=1, row=0)

        # False Button
        self.false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_img)
        self.false_button.grid(column=1, row=3)

        # True Button
        self.true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_img)
        self.true_button.grid(column=0, row=3)


        self.window.mainloop()
