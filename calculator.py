from tkinter import *

root = Tk()

#Displays my name on the Window Description
root.title("Paul Calculator")



#Here are the functions for the buttons I created

def click(num):
    current_entry = e.get()
    e.delete(0, END)
    e.insert(0, str(current_entry) + str(num))

def clear():
    e.delete(0, END)

def add_button():
    current_number = e.get()
    global first_number
    first_number = int(current_number)
    e.delete(0, END)
    
    

def equal_button():
    current_number = e.get()
    global second_number
    second_number = int(current_number)
    total = int(first_number) + int(second_number)
    e.delete(0, END)
    e.insert(0, str(total))

  


#Entry Field where you can type numbers inside or see the numbers inserted after pressing the buttons
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0,  columnspan=3, padx=10, pady=10)



#Here I define all the buttons
num_1 = Button(root, text="1", padx=40, pady=20, command=lambda:click(1))
num_2 = Button(root, text="2", padx=40, pady=20, command=lambda:click(2))
num_3 = Button(root, text="3", padx=40, pady=20, command=lambda:click(3))

num_4 = Button(root, text="4", padx=40, pady=20, command=lambda:click(4))
num_5 = Button(root, text="5", padx=40, pady=20, command=lambda:click(5))
num_6 = Button(root, text="6", padx=40, pady=20, command=lambda:click(6))

num_7 = Button(root, text="7", padx=40, pady=20, command=lambda:click(7))
num_8 = Button(root, text="8", padx=40, pady=20, command=lambda:click(8))
num_9 = Button(root, text="9", padx=40, pady=20, command=lambda:click(9))

num_0 = Button(root, text="0", padx=40, pady=20, command=lambda:click(0))

clear_button = Button(root, text="Clear", padx=79, pady=20, command=lambda:clear())
button_add = Button(root, text="+", padx=39, pady=20, command=add_button)
button_equal = Button(root, text="=", padx=91, pady=20, command=equal_button)


#Here I add all the buttons to the screen using the grid method
num_1.grid(row=3, column=0)
num_2.grid(row=3, column=1)
num_3.grid(row=3, column=2)

num_4.grid(row=2, column=0)
num_5.grid(row=2, column=1)
num_6.grid(row=2, column=2)

num_7.grid(row=1, column=0)
num_8.grid(row=1, column=1)
num_9.grid(row=1, column=2)


num_0.grid(row=4, column=0, )
clear_button.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)








root.mainloop()