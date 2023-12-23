
import pynput                #disable mouse and keyboard input
import keyboard
from tkinter import *
from tkinter import messagebox

mouse_listener = pynput.mouse.Listener(suppress=True)
keyboard_listener = pynput.keyboard.Listener(suppress=True)


def disable_keyboard():   #function to disable the keyboard
    keyboard_listener = pynput.keyboard.Listener(suppress=True)
    keyboard_listener.start()
    if messagebox.askokcancel(title='to Leave', message='to re-enable the keyboard:\n'
                                                     '1. just exit the program.\n'
                                                     '2. press ok or cancel.'):
        keyboard_listener.stop()
    else:
        keyboard_listener.stop()


def disable_mouse():    #function to disable the mouse
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()
    messagebox.showinfo(title='to Leave', message='to re-enable the mouse:\n'
                                                  '1. just exit the program.\n'
                                                  '2. press enter then shift+R.')
    keyboard.wait('shift+r')
    mouse_listener.stop()


def read_me_btn():  #the message when read me is pressed
    messagebox.showinfo(title='Info!', message='This program can be used if you want to clean your keyboard or/and mouse.\n')

def main():
    #the gui stuff
    global mouse_listener, keyboard_listener
    window = Tk()

    window.geometry('600x600')
    window.title('input Disabler')
    icon = PhotoImage(file='icons8-keyboard-68.png')
    window.iconphoto(True, icon)
    window.config(background='#9b9b9b')

    label = Label(window, text='Welcome.\nyou can disable/enable the keyboard or mouse here.'
                               '\n***Please dont try disabling both at the same time***'
                               '\n\n\n')
    label.config(background='#9b9b9b', foreground='#b80000',font=('Arial', 16, 'bold'))
    label.pack()

    dis_keyboard_btn = Button(window, text='Disable Keyboard', command=disable_keyboard, font=('Comic Sans', 20), foreground='#b80000',width=15)
    dis_keyboard_btn.pack()

    label2 = Label(window, text='\n\n\n', background='#9b9b9b')
    label2.pack()

    dis_mouse_btn = Button(window, text='Disable Mouse', command=disable_mouse, font=('Comic Sans', 20), foreground='#b80000', width=15)
    dis_mouse_btn.pack()

    label3 = Label(window,text='\n\n\n', background='#9b9b9b')
    label3.pack()

    readme_btn = Button(window, text='Read Me!', font=('Comic Sans', 20), command=read_me_btn, foreground='#b80000', width=15)
    readme_btn.pack()

    label3 = Label(window, text='\n\n\n\n\n Made by Hasan, just for fun and giggles!', background='#9b9b9b')
    label3.config(background='#9b9b9b', foreground='#b80000', font=('Arial', 16, 'bold'))
    label3.pack()

    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window))

    window.mainloop()


def on_close(window):
    # Stop listeners before closing the window
    keyboard_listener.stop()
    mouse_listener.stop()
    window.destroy()


main()
