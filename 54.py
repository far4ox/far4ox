from tkinter import *

def btn_click(item):
    global expression 
    try:
        input_falied['state']= 'normal'
        expression += item 
        input_falied.insert (END, item)

        if item == '=':
            result = str(eval (expression[:-1]))
            input_falied.insert(END, result)
            expression = ' '
        input_falied['state'] = 'readonly'

    except ZeroDivisionError:
        input_falied.delete (0, END)
        input_falied.insert (0, 'Не дели на 0, придурок')
    except SyntaxError:
        input_falied.delete (0, END)
        input_falied.insert (0, 'молодец, придурок')

def bt_clear ():
    global expression
    expression = ' '
    input_falied['state'] = 'normal'
    input_falied.delete (0, END)
    input_falied['state'] = 'readonly'




root = Tk()
root.geometry ('320x360')
root.title ('calculater')
root.resizable (width=False, height=False)

frame_input = Frame(root)
frame_input.grid (row=0, column=0, columnspan=4, sticky="nsew")
input_falied = Entry(frame_input, font='Arial 15', width=24, state = 'readonly')

input_falied.pack(fill=BOTH)

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

expression = ' '

buttonclear = Button(root, text='c', command = lambda: bt_clear())
buttonclear.grid(row=1, column=3, sticky='nsew')

for row in range (4):
    for col in range (4):
        Button(root, width=2, height=3, text=buttons[row][col], command=lambda row=row, col=col: btn_click(buttons[row][col])).grid \
        (row=row + 2, column=col, sticky='nsew', padx=1, pady=1)


root.mainloop()