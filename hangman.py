import random
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("720x540")
root.resizable(False, False)
root.configure(background="black")
canvas = Canvas(bg="yellow")

def hangman():
    #face and rope and body
    canvas.create_line(360, 0, 360, 70, width="3")
    canvas.create_oval(340, 70, 380, 110, outline="black", width=5)
    canvas.create_line(360, 110, 360, 150, width="3")
    #hands
    canvas.create_line(360, 120, 340, 150, width=3)
    canvas.create_line(360, 120, 380, 150, width=3)
    #legs
    canvas.create_line(360, 150, 340, 180, width="3")
    canvas.create_line(360, 150, 380, 180, width="3")
    canvas.pack(fill="x")
hangman()

f = Frame(root, background="black", width=720, height=20)
for i in range(7):
    f.columnconfigure(i, weight=1)
for i in range(4):
    f.rowconfigure(i, weight=1)

key = StringVar()

E = Entry(root, textvariable=key, background = "yellow", font="TimesNewRoman 20 bold", width=5)
l1 = Label(root, text="Your guess: ", font="TimesNewRoman 14", background="black", foreground="white")

start = Button(f, text="Start", width=20, height=4, background="white", foreground="black")
start.grid(row=1, column=2, columnspan=3)


def updater(lis):
    for i in range(5):
        l1 = Label(f, text=lis[i], background="black", foreground="white", font="TimesNewRoman 18")
        l1.grid(row=1, column=i+1, sticky='nsew') 

def submitted(key, word, lis):
    str1 = key.get()
    checker(str1[0], word, lis)
    updater(lis)
    global count
    res = fullword(lis)
    if res == word:
        response = messagebox.askretrycancel("You won!", f"It took you {count} tries!")
        if response:
            hangman()
            startgame(1)
            key.set("")
    else:
        count += 1
        key.set("")
        E.update()

def fullword(hidden):
    res = ""
    for i in hidden:
        res+= i
    return res

def checker(letter, word, lis):
    if letter in word:
        for i, x in enumerate(word):
            if letter == x:
                lis[i] = x
    else:
        lifeloss()
    return lis

def lifeloss():
    global lives
    lives-=1
    match(lives):
        case 5:
            canvas.create_line(360, 120, 340, 150, width=3, fill="yellow")
        case 4:
            canvas.create_line(360, 120, 380, 150, width=3, fill="yellow")
        case 3:
           canvas.create_line(360, 150, 340, 180, width="3", fill="yellow")
        case 2:
            canvas.create_line(360, 150, 380, 180, width="3", fill="yellow")
        case 1:
            canvas.create_line(360, 110, 360, 150, width="3", fill="yellow")
        case 0:
            response = messagebox.askretrycancel("Game over!", "Lol ur so bad XD")
            if response:
                hangman()
                startgame(1)
            else:
                root.quit()
    return

submit = Button(root, text="Enter", height=1, width=3)

def startgame(e):
    global lives, count
    lives = 6
    count = 0
    start.destroy()
    fh=open("words.txt","r")
    words=list(map(str.strip, fh.readlines()))
    fh.close()
    while True:
        word = random.choice(words)
        if len(word) == 5:
            break

    hidlis=["_", "_", "_", "_", "_"]

    l1.pack(side=LEFT, padx=10)
    E.pack(side=LEFT, padx=10)
    submit.pack(side=LEFT, padx=10)
    submit.bind('<Button-1>', lambda e: submitted(key, word, hidlis))
    

    updater(hidlis)
    print(word)
f.pack(fill="both", expand=True)
start.bind('<Button-1>', startgame)

root.mainloop()
