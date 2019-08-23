import tkinter
from tkinter import *
import random
from tkinter import messagebox


words = [
    "love/of others/good manners/and/win the/respect",
    "when/best/they can/one is/be learnt/young",
    "saves us/turns away/soft answer / anger and /a/ a pitfall/ from many",
    "who is/ stranger/ respectful/ a person / even/ like",
    "sure / in life/ they/ passport/ are a/ for success",
    "h v e e i c a",
    "m t r u a a e",
    "c n i n t a e",
    "m c e x p o l",
    "o o c d e r k",
    "t o e y r s d",
    "e g v n i n e",
    "i n i f t c o",
    "o h l f i o s",
    "o g e f i r v",
    "r e e t p s n",
    "e s d e d c n",
    "l h a o w l s",
    "n o n g r i m",
    "i c e e v e r",
    "l u i e n c d",
    "r d m i a r e",
    "i m m m a x u"
]

answers = [
    "good manners win the love and respect of others",
    "they can be learnt best when one is young",
    "a soft answer turns away anger and saves us from many a pitfall",
    "even strangers like a person who is respectful",
    "they are a sure passport for success in life",
    "achieve",
    "amateur",
    "ancient",
    "complex",
    "crooked",
    "destroy",
    "evening",
    "fiction",
    "foolish",
    "forgive",
    "present",
    "descend",
    "shallow",
    "morning",
    "receive",
    "include",
    "married",
    "maximum"
]

num = random.randrange(0,24,1)

def res():
    global words, answers, num
    num = random.randrange(0,24,1)
    lbl.config(text = words[num])
    e1.delete(0,END)
    lbl2.delete(0, END)

def default():
    global  words,answers,num
    lbl.config(text = words[num])

def show():
    global words,answers,num
    lbl2.config(text = answers[num])


def checkans():
    global words,answers,num
    var = e1.get()

    if var == answers[num]:
        messagebox.showinfo("HURRAY!","This is a correct answer.")
        res()
    else:
        messagebox.showerror("ERROR","you make it wrong")
        e1.delete(0,END)



root = tkinter.Tk()
root.geometry("400x400+400+400")
root.title("Jumble Game")
root.configure(background="#000000")

lbl = Label(
    root,
    text = "your Text here",
    font = ("verdana",18),
    bg = "#000000",
    fg = "#ffffff",
)

lbl.pack(pady = 30,ipady = 10, ipadx = 10)

lbl2 = Label(
    root,
    text = "Answer",
    font = ("verdana",18),
    bg = "#000000",
    fg = "#ffffff",
)

lbl2.pack(pady = 30,ipady = 10, ipadx = 10)

#ans1 = StringVAr()

e1 = Entry(
    root,
    font = ("verdana",16),
    #textvariable = ans1,
)

e1.pack(ipady = 5, ipadx = 5)

btncheck = Button(
    root,
    text = "check",
    font = ("Comic sans ms",16),
    width = 16,
    bg = "#4c4bab",
    fg = "#6ab04c",
    relief = GROOVE,
    command = checkans,
)
btncheck.pack(pady = 40)

btnreset = Button(
    root,
    text = "Reset",
    font = ("Comic sans ms",16),
    width = 16,
    bg = "#4c4bab",
    fg = "#EA42AC",
    relief = GROOVE,
    command = res,
)
btnreset.pack()

btnshow = Button(
    root,
    text = "Answer",
    font = ("Comic sans ms",16),
    width = 16,
    bg = "#2eaf56",
    fg = "#EA42AC",
    relief = GROOVE,
    command = show,
)
btnshow.pack(pady = 20)

default()

root.mainloop()