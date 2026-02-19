from tkinter import*
root =Tk()

# creating title for root
root.title("python Tkmod")

label1 =Label(root,text ="Hello World")
label2 =Label(root,text ="Hello Covid")
# when grid use then initial the row and column
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)

root.mainloop()
