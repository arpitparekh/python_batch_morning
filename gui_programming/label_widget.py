import tkinter as tk

# Create a window
root = tk.Tk()
root.title("My GUI")
root.geometry("400x400")
root.configure(bg="lightblue",bd=20,relief="raised")
# stop resizing
root.resizable(False,False)


# root is my main widget
label = tk.Label(root, text="Hello, Tkinter!",fg="red",bg="yellow",font=("Arial", 16),bd=10,cursor="hand2")

# label.place(x=100, y=50)
# label.pack()
label.grid(row=0,column=0)

tk.Label(root, text="Hello, Tkinter!",fg="white",bg="black",font=("Arial", 16),bd=10,cursor="hand2",underline=10,relief="raised").grid(row=1,column=2)

root.mainloop()
