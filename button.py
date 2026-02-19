from tkinter import*
root = Tk()
def myButton():
    mylabel =Label(root,text="you are a proggramer")
    mylabel.grid(row= 1, column=0)
    
    
#if add a button take a variable call=mybtn and add it with "grid"
#if i call "command" and mention that when i click the button the result will come "you are a proggramer".
# if i want to click the button and the result will show in root then use "mylabel"

mybtn = Button(root,text = "Click", fg="red",bg="green",padx=10,pady=15, command=myButton)

mybtn.grid(row=0, column=1)



root.mainloop()
