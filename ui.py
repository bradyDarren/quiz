from tkinter import *
from quizbrain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface: 

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady= 20, bg=THEME_COLOR)


        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.question = self.canvas.create_text(
            150,
            125,
            width=280, # by setting the width to be less than the window it will automatically
            # wrap the text
            text="Question",
            font=('Ariel',20, 'italic'),
            fill='black'
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, pady=20, fg='white')
        self.score.grid(column=1, row=0)

        # False Button
        self.false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_img, command=self.false_button_press)
        self.false_button.grid(column=1, row=3)

        # True Button
        self.true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_img, command=self.true_button_press)
        self.true_button.grid(column=0, row=3)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg='white')
        if self.quiz.remaining_questions:
            self.score.config(text=f"Score:{self.quiz.answers_correct}")
            q_text = self.quiz.get_next_question()
            self.canvas.itemconfig(self.question, text = q_text)
        else: 
            self.canvas.itemconfig(self.question, text = "You have reached the end of the quiz.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true_button_press(self):
        self.give_feedback(self.quiz.check_answer('True'))
    
    def false_button_press(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg='green')
        else: 
            self.canvas.config(bg='red')
        
        self.window.after(1000,self.get_question)