# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter
import os

mainWindow_padding = 8
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480+8+200')
mainWindow['padx'] = mainWindow_padding

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=5, sticky='nsew')

calculatorFrame = tkinter.Frame(mainWindow)
calculatorFrame.grid(row=1, column=0, sticky='nsew')
# canvas = tkinter.Canvas(calculatorFrame)
# canvas.grid(row=0, column=0, sticky='n')


# mainWindow.columnconfigure(0, weight=1)
# mainWindow.rowconfigure(0, weight=1)

buttonText = [['C', 'CE'],
              ['7', '8', '9', '+'],
              ['4', '5', '6', '-'],
              ['1', '2', '3', '*'],
              ['0', '=', '/']
]

# Alt version, has column span in list
# buttonText = [[('C', 1), ('CE', 1)],
#               ['7', '8', '9', '+'],
#               ['4', '5', '6', '-'],
#               ['1', '2', '3', '*'],
#               ['0', '=', '/']
# ]

for row, buttons in enumerate(buttonText):
    for col, button in enumerate(buttons):
        span = 1
        if button == '=':
            span = 2
        tempButton = tkinter.Button(calculatorFrame, text=button)
        print(button, row, col, span)
        tempButton.grid(row=row, column=col, columnspan=span, sticky='ew')
        # mainWindow.columnconfigure(col, weight=1)
        # mainWindow.rowconfigure(row, weight=1)


mainWindow.update()
# mainWindow.minsize(width=150, height=250)
min_width = calculatorFrame.winfo_width() + mainWindow_padding
min_height = calculatorFrame.winfo_height() + result.winfo_height()
mainWindow.minsize(min_width, min_height)
mainWindow.maxsize(min_width + 50, min_height + 50)

mainWindow.mainloop()
