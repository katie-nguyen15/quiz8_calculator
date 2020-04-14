from tkinter import *
from tkinter import font as tkFont
import math


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")


def btnEqualsInput():
    global operator
    try:
        evaluate = str(eval(operator))
        operator = evaluate
    except:
        evaluate = "error"
    text_input.set(evaluate)


def btnSquareRoot():
    global operator
    evaluate = str(math.sqrt(eval(operator)))
    text_input.set(evaluate)
    operator = evaluate


def btnSquared():
    global operator
    evaluate = str(eval(operator + "**2"))
    text_input.set(evaluate)
    operator = evaluate


def btnDelete():
    global operator
    operator = operator[:-1]
    text_input.set(operator)


def enlarge():
    global fontSize
    fontSize.configure(size = fontSize.cget('size') + 1)


def shrink():
    global fontSize
    fontSize.configure(size = fontSize.cget('size') - 1)


def main():
    global operator, text_input, fontSize
    cal = Tk()
    cal.title("Calculator")
    operator = ""
    text_input = StringVar()
    fontSize = tkFont.Font(family="ariel", size=15, weight="bold")
    xPad = 16
    yPad = 16

    txtDisplay = Entry(cal, font=fontSize,
                       textvariable=text_input,
                       bd=15, insertwidth=3, bg="powder blue",
                       justify='right').grid(columnspan=5)
    # 7, 8 ,9
    btn7 = Button(cal, font=fontSize, padx=16, pady=16,
                  bd=8, fg="black", text="7",
                  command=lambda: btnClick(7)).grid(row=1, column=0)
    btn8 = Button(cal, font=fontSize, padx=16, pady=16,
                  bd=8, fg="black", text="8",
                  command=lambda: btnClick(8)).grid(row=1, column=1)
    btn9 = Button(cal, font=fontSize, padx=16, pady=16,
                  bd=8, fg="black", text="9",
                  command=lambda: btnClick(9)).grid(row=1, column=2)
    # 4, 5, 6
    btn4 = Button(cal, font=fontSize, padx=16, pady=16,
                  bd=8, fg="black", text="4",
                  command=lambda: btnClick(4)).grid(row=2, column=0)
    btn5 = Button(cal, font=fontSize, padx=16, pady=16,
                  bd=8, fg="black", text="5",
                  command=lambda: btnClick(5)).grid(row=2, column=1)
    btn6 = Button(cal, font=fontSize, padx=16, pady=16,
                  bd=8, fg="black", text="6",
                  command=lambda: btnClick(6)).grid(row=2, column=2)
    # 1, 2, 3
    btn1 = Button(cal, font=fontSize, padx=16, pady=16,
                  bd=8, fg="black", text="1",
                  command=lambda: btnClick(1)).grid(row=3, column=0)
    btn2 = Button(cal, font=fontSize, padx=16, pady=16,
                  bd=8, fg="black", text="2",
                  command=lambda: btnClick(2)).grid(row=3, column=1)
    btn3 = Button(cal, font=fontSize, padx=16, pady=16,
                  bd=8, fg="black", text="3",
                  command=lambda: btnClick(3)).grid(row=3, column=2)
    # C, 0, =
    btn1Clear = Button(cal, font=fontSize, padx=16, pady=16,
                       bd=8, fg="black", text="C",
                       command=btnClearDisplay).grid(row=4, column=0)
    btn0 = Button(cal, font=fontSize, padx=16, pady=16,
                  bd=8, fg="black", text="0",
                  command=lambda: btnClick(0)).grid(row=4, column=1)
    btnEquals = Button(cal, font=fontSize, padx=16, pady=16,
                       bd=8, fg="black", text="=",
                       command=btnEqualsInput).grid(row=4, column=2)
    # + , - , *, /
    btnAdd = Button(cal, font=fontSize, padx=16, pady=16,
                    bd=8, fg="black", text="+",
                    command=lambda: btnClick("+")).grid(row=1, column=3)
    btnSub = Button(cal, font=fontSize, padx=16, pady=16,
                    bd=8, fg="black", text="-",
                    command=lambda: btnClick("-")).grid(row=2, column=3)
    btnMul = Button(cal, font=fontSize, padx=16, pady=16,
                    bd=8, fg="black", text="*",
                    command=lambda: btnClick("*")).grid(row=3, column=3)
    btnDiv = Button(cal, font=fontSize, padx=16, pady=16,
                    bd=8, fg="black", text="/",
                    command=lambda: btnClick("/")).grid(row=4, column=3)

    # sqrt, ^, ^2, back
    btnSqrt = Button(cal, font=fontSize, padx=16, pady=16,
                     bd=8, fg="black", text="√",
                     command=btnSquareRoot).grid(row=5, column=0)
    btnPow = Button(cal, font=fontSize, padx=16, pady=16,
                    bd=8, fg="black", text="^",
                    command=lambda: btnClick("**")).grid(row=5, column=1)
    btnSquare = Button(cal, font=fontSize, padx=16, pady=16,
                       bd=8, fg="black", text="^2",
                       command=btnSquared).grid(row=5, column=2)
    btnDel = Button(cal, font=fontSize, padx=16, pady=16,
                    bd=8, fg="black", text="↵",
                    command=btnDelete).grid(row=5, column=3)
    
    # enlarge, shrink
    btnEnlarge = Button(cal, font=fontSize, padx=xPad * 2,
                        pady=yPad, bd=8, fg="black", text="enlarge",
                        command=enlarge).grid(row=6, column=0, columnspan=2)
    btnShrink = Button(cal, font=fontSize, padx=xPad * 2, pady=yPad,
                       bd=8, fg="black", text="shrink",
                       command=shrink).grid(row=6, column=2, columnspan=2)
    
    cal.mainloop()


if __name__ == "__main__":
    main()
