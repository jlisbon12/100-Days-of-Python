import random
from tkinter import *
import pandas
import random

# ---------------------------- DISPLAY PORTUGUESE WORDS ------------------------------- #
words = {}
words_dict = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("data/portuguese_words.csv")
    words_dict = original.to_dict('records')
else:
    words_dict = data.to_dict('records')


def learning():

    global words, flip
    window.after_cancel(flip)
    words = random.choice(words_dict)
    canvas.itemconfig(card, image=front_card)
    canvas.itemconfig(title, text="Portuguese", fill='black')
    canvas.itemconfig(word, text=words['Portuguese'], fill='black')
    flip = window.after(3000, func=change_card)

def learnt():
    global words
    words_dict.remove(words)
    known_data = pandas.DataFrame(words_dict)
    known_data.to_csv("data/words_to_learn.csv", index=False)
    learning()



def change_card():
    global words
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=words['English'], fill='white')


window = Tk()
window['background'] = '#B1DDC5'
window.title("flashLang")
window.minsize(width=900, height=700)
window.config(padx=50, pady=50)

flip = window.after(3000, func=change_card)
canvas = Canvas(width=800, height=526, bg='#B1DDC5', highlightthickness=0)

back_card = PhotoImage(file="img/card_back.png")
front_card = PhotoImage(file="img/card_front.png")
card = canvas.create_image(403, 267, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

g_img = PhotoImage(file="img/right.png")
check_btn = Button(image=g_img, borderwidth=0, highlightthickness=0, command=learnt)
check_btn.grid(row=1, column=1)

r_img = PhotoImage(file="img/wrong.png")
cross_btn = Button(image=r_img, borderwidth=0, highlightthickness=0, command=learning)
cross_btn.grid(row=1, column=0)

title = canvas.create_text(400, 160, text="", font=("Arial", 40, "italic"), fill='black')
word = canvas.create_text(400, 273, text="", font=("Arial", 60, "bold"), fill='black')

learning()




window.mainloop()
