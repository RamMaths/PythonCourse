import tkinter

window = tkinter.Tk()
window.title("window")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

#Entry
input = tkinter.Entry(width=10)
input.grid(row=0, column=3)

#Label
my_label = tkinter.Label(text="Miles")
my_label.grid(row=0, column=4)

#Label
my_label = tkinter.Label(text="is equal to")
my_label.grid(row=1, column=1)

#Label
my_label = tkinter.Label(text="result")
my_label.grid(row=1, column=3)

#Label
my_label = tkinter.Label(text="Km")
my_label.grid(row=1, column=4)

#button
button = tkinter.Button(text="Calculate")
button.grid(row=1, column=1)

#Entry
input = tkinter.Entry(width=10)
input.grid(row=2, column=3)


window.mainloop()
