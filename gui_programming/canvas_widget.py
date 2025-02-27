from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("My GUI")
root.geometry("400x400")

canvas = Canvas(root,width=400,height=400,bg="lightblue")
canvas.pack()

canvas.create_line(0,0,400,400,fill="red",width=5)
canvas.create_rectangle(50,50,100,100,fill="green")
canvas.create_rectangle(200,200,250,350,fill="orange")
canvas.create_rectangle(300,300,350,350,fill="yellow")
canvas.create_oval(150,150,350,350,fill="black")
canvas.create_text(250,250,text="Hello",font=("Arial", 16),fill="white")

image = Image.open("/home/arpit-parekh/Downloads/bascom_projects/python_batch_morning/gui_programming/images/photo.jpeg")

resized_image = image.resize((100, 100))

photo = ImageTk.PhotoImage(image)

canvas.create_image(200,200,image=photo)

root.mainloop()
