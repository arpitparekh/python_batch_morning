from tkinter import *
# Create a window
root = Tk()
root.title("My GUI")
root.geometry("400x400")


number = IntVar(root)   # statevariable
number.set(0)

label = Label(root, text=number.get(),fg="red",bg="yellow",font=("Arial", 16),bd=10,cursor="hand2")
label.pack()


def clickKyaRe():
  number.set(number.get()+1)
  label.config(text=number.get())

button = Button(root, text="Click me!",command=clickKyaRe)
button.pack()

root.mainloop()
