from tkinter import *

root = Tk()
root.title("UserForm")
root.geometry("350x600")

firstName = StringVar()
lastName = StringVar()
password = StringVar()
codingCheckValue = StringVar()
cyclingCheckValue = StringVar()
genderValue = StringVar()

def submitClick():
  code = ""
  if codingCheckValue.get() == "Coding":
    code += "Coding "
  if cyclingCheckValue.get() == "Cycling":
    code += "Cycling "

  result = f"First Name: {firstName.get()}\nLast Name: {lastName.get()}\nPassword: {password.get()} \nHobbies: {code}\n Gender: {genderValue.get()} \n City: {cityVar.get()} \n Confidence: {confidenceVar.get()}"
  resultLabel.config(text=result)

  firstNameEntry.delete(0,END)
  lastNameEntry.delete(0,END)
  passwordEntry.delete(0,END)
  codingCheckValue.set("")
  cyclingCheckValue.set("")
  genderValue.set("")
  cityVar.set("Select City")
  confidenceVar.set(0)


firstNameLabel = Label(root,text="First Name")
firstNameLabel.pack()
firstNameEntry = Entry(root,width=20,textvariable=firstName)
firstNameEntry.pack()

lastNameLabel = Label(root,text="Last Name")
lastNameLabel.pack()
lastNameEntry = Entry(root,width=20,textvariable=lastName)
lastNameEntry.pack()

passwordLabel = Label(root,text="Password")
passwordLabel.pack()
passwordEntry = Entry(root,width=20,textvariable=password,show="*")
passwordEntry.pack()

codingButton = Checkbutton(text="Coding",onvalue="Coding",offvalue="",variable=codingCheckValue)
codingButton.pack()
cyclingButton = Checkbutton(text="Cycling",onvalue="Cycling",offvalue="",variable=cyclingCheckValue)
cyclingButton.pack()

maleRadio = Radiobutton(text="Male",value="Male",variable=genderValue)
maleRadio.pack()
femaleRadio = Radiobutton(text="Female",value="Female",variable=genderValue)
femaleRadio.pack()

mb = Menubutton(root,text="Select City",relief=RAISED)
mb.menu = Menu(mb)
mb["menu"] = mb.menu

def update_button_text(*args):
    mb["text"] = cityVar.get()

cityVar = StringVar()
cityVar.trace_add('write', update_button_text)

mb.menu.add_radiobutton(label="Ahmedabad",variable=cityVar)
mb.menu.add_radiobutton(label="Surat",variable=cityVar)
mb.menu.add_radiobutton(label="Rajkot",variable=cityVar)
mb.menu.add_radiobutton(label="Vadodara",variable=cityVar)

mb.pack()

confidenceLabel = Label(root,text="Confidence")
confidenceLabel.pack()
confidenceVar = IntVar()
confidenceScale = Scale(root,from_=0,to=100,orient=HORIZONTAL,length=200,variable=confidenceVar)
confidenceScale.pack()

button = Button(root,text="Submit",command=submitClick)
button.pack()

resultLabel = Label(root,text="")
resultLabel.pack()

root.mainloop()
