# Step 1. Importing moduls
from tkinter import *  
from tkinter import messagebox
from PIL import ImageTk, Image


def new_task():
    task = entry_box.get()
    if task != "":
        lbox1.insert(END, task)
        entry_box.delete(0, "end")
    else:
        messagebox.showwarning("Please enter some task.")
# Messagebox is used to display an error message when the
# user clicks on the add button with an empty
# entry box.



def delete_task():
    lbox1.delete(ANCHOR) #ANCHOR refers to the selected item in the Listbox.



# Step 2. Creating the window
windows = Tk()  
windows.geometry('450x450+450+200')  
windows.title('Your daily tasks ')  
windows.resizable(width=True, height=True)  
img = ImageTk.PhotoImage(Image.open("woodlights.png"))
windows.config(bg='#6C331C')


# Step 3. Creating a frame
# Frame widgets are used to hold other widgets. We will place Listbox, scrollbars & buttons inside the frame.
frame = Frame(windows)
frame.pack(pady=10)  #I've added extra padding around the frame from outside.
label = Label(frame, image = img)
label.pack()
# Step 4. Adding Listbox
lbox1 = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 14),  #Times New Roman font is provided with 14 sizes
    border=0,
    fg='#464646', # foreground color or the text color.
    highlightthickness=0,
    selectbackground='#F19D7B',  # this function decides the color of the focused item in the Listbox.
    activestyle="none", # with this step we remove the underline that appears when the item is selected or focused.
    
)

lbox1.pack(side=LEFT, fill=BOTH)  #side-Left keeps the Listbox to the left side and 
# allows to put the scrollbars to the right side.
# fill=BOTH allows to fill the blank space in both the directions that are x and y

# Step 5. Adding dummy data
# We have added dummy data so that the application is ready to view. 
# You add or delete whatever data you want.

mylist = [
    'Read 50 pages',
    '30 minutes of English',
    'walking 1 hour',
    'write an essay',
    'zoom meeting' 
    ]


for item in mylist:
    lbox1.insert(END, item) # END signifies that a new item will be added in the end. 
    # If END is replaced with 0 then new data will be added at the top.


# Step 6. Adding scrollbars 
scbar = Scrollbar(frame)
scbar.pack(side=RIGHT, fill=BOTH)
lbox1.config(yscrollcommand=scbar.set) # we have bind Listbox with scrollbar
scbar.config(command=lbox1.yview) #  here yview means scrollbar will go in the vertical direction.
# If it would have been xview then the scrollbar would have worked in the horizontal direction.

# Step 7. Adding entry box
entry_box=Entry(
    windows,
    font=('Times', 14)
)
entry_box.pack(pady=20)

# Step 8. Creating a frame for buttons
frforbuttons = Frame(windows)
frforbuttons.pack(pady=20)

# Step 9. Another buttons
# adding a new task
add_task_btn = Button(
    frforbuttons,
    text='Add Task',
    font=('Times',14),
    bg='#5A1904',
    fg='#FFFFFF',
    padx=20,
    pady=10,
    command = new_task
)
add_task_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Deleting the task

del_task_btn = Button(
    frforbuttons,
    text='Delete Task',
    font=('Times 14'),
    bg='#5A1904',
    fg='#FFFFFF',
    padx=20,
    pady=10,
    command= delete_task
)
del_task_btn.pack(fill=BOTH, expand=True, side=LEFT)

windows.mainloop()

 




