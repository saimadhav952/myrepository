from tkinter import *
from string import *
from secrets import *
import pyperclip as pp


def generate():
    give.delete('0', 'end')
    if checkVar.get() == 1:
        passw = ascii_letters + digits + punctuation
        while True:
            a = ''
            alphabet_lower = 0
            alphabet_upper = 0
            digit_count = 0
            special_count = 0
            for j in range(int(qw.get())):
                k = choice(passw)
                if k.islower():
                    alphabet_lower += 1
                elif k.isupper():
                    alphabet_upper += 1
                elif k.isdigit():
                    digit_count += 1
                elif k in punctuation:
                    special_count += 1
                a += k
            if alphabet_lower >= 1 and alphabet_upper >= 1 and digit_count >= 1 and special_count >= 1:
                give.insert(0, a)
                break
    elif checkVar.get() == 0:
        passwo = ascii_letters + digits
        while (True):
            a = ''
            alphabet_lower = 0
            alphabet_upper = 0
            digit_count = 0
            special_count = 0
            for j in range(int(qw.get())):
                k = choice(passwo)
                if k.islower():
                    alphabet_lower += 1
                elif k.isupper():
                    alphabet_upper += 1
                elif k.isdigit():
                    digit_count += 1
                elif k in punctuation:
                    special_count += 1
                a += k
            if alphabet_lower >= 1 and alphabet_upper >= 1 and digit_count >= 1:
                give.insert(0, a)
                break


def cop():
    pp.copy(give.get())


window = Tk()
window.geometry('500x300')
window.resizable(FALSE, FALSE)
window.title('Password Generator')
frame = LabelFrame(window, text="Password Generator", bg='#FFF8DC', labelanchor='n', font=('Helvetica', 18, 'bold'),
                   fg='#458B74')
frame.pack(expand=True, fill=BOTH)
Label(frame, text='Password length :', font=('Helvetica', 14), bg='#FFF8DC').place(anchor='w', x=20, y=30)
Label(frame, text='Generated Password :', font=('Helvetica', 14), bg='#FFF8DC').place(anchor='w', x=20, y=80)
qw = IntVar()
take = Entry(frame, relief='groove', font=('Helvetica', 14), textvariable=qw)
take.place(x=200, y=20, width=100)
give = Entry(frame, relief='groove', font=('Helvetica', 14))
give.place(x=250, y=68)
Button(frame, text="GENERATE", bg='cadet blue1', relief='groove', font=('Times', 10), command=generate).place(x=160,
                                                                                                              y=190)
Button(frame, text="COPY", bg='cadet blue1', relief='groove', font=('Times', 10), command=cop).place(x=260, y=190)
give.bind("<KeyPress>", lambda q: "break")
checkVar = IntVar()
check_special = Checkbutton(text="special characters", variable=checkVar, bg='#FFF8DC')
check_special.place(x=180, y=150)
window.mainloop()

