import tkinter

window = tkinter.Tk()
window.title("window")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="Hello world!")
my_label.grid(row=0, column=0)

#button
button = tkinter.Button(text="Button1")
button.grid(row=0, column=2)

#button
button = tkinter.Button(text="Button2")
button.grid(row=1, column=1)

#Entry
input = tkinter.Entry(width=10)
input.grid(row=2, column=3)


window.mainloop()
