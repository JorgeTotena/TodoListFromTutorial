from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        #defines the root
        self.root = root
        #changes the title of the window
        self.root.title('To-do-list')
        #Defines the dimension of the window
        self.root.geometry('650x410+300+150')
        self.label = Label(self.root, text='To-Do-List-App', 
            font='arial, 25 bold', width=10,bd=5, bg='skyblue4', fg='black')
        self.label.pack(side='top', fill=BOTH)
        self.label2 = Label(self.root, text='Add Task', 
            font='arial, 18 bold', width=10,bd=5, bg='SkyBLue2', fg='black')
        # places the label into a specific coordinates
        self.label2.place(x=40, y=54)
        self.label3 = Label(self.root, text='Tasks', 
            font='arial, 18 bold', width=10,bd=5, bg='SkyBLue2', fg='black')
        # places the label into a specific coordinates
        self.label3.place(x=320, y=54)
        
        #Creates a list box within the root
        self.main_text = Listbox(self.root, height=9, bd=5, width=18, font="arial, 20 italic bold")
        self.main_text.place(x=280, y= 100)
        
        #The text function allows you to create an input box
        self.text = Text(self.root, bd=5, height=2, width=25, font='arial, 10 bold')
        self.text.place(x=20, y=120)
    
    #===============================ADD TASK ============================= #
    
    #
    
def add():
    # The get method retrieves the text contained within the widget. It takes two arguments:
    # 1.0 and END. These arguments specify the range of text to retrieve, where 
    # 1.0 represents the first character of the first line and END represents 
    # the end of the text in the widget.
    content = self.text.get(1.0, END)
    # Here we're inserting it into the listbox
    self.main_text.insert(END, content)
    #Opening the file and adding the content
    with open('data.txt', "a") as file:
        file.write(content)
        #Offset to the beginning of the file at "0"
        file.seek(0)
        file.close()
    #Clears the text of the input box after you do the input process
    self.text.delete(1, 0, END)
    
def delete_():
    #Selects what I'm currently clicking with my mouse
    delete = self.main_text.curselection()
    #What's on the seleccion?
    look = self.main.text.get(delete_)
    with open('data.txt', 'r+') as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            item = str(look)
            # if the item that i selected is not within the lines, then it will
            # rewrite the lines with the ones that should not be deleted
            if item not in line:
                f.write(line)
        f.truncate()
def main():
    # defines the main window of the program
    root = Tk()
    ui = todo(root)
    root.mainloop()
    
if __name__ =="__main__":
    main()
    
    
    
''' seek(0) is a method in Python's file object that sets the current file position to the offset 0. This means that the next read or write operation will take place at the beginning of the file. The seek method takes two arguments: the offset, and the reference point from which the offset is calculated. In this case,
the offset is 0 and the reference point is the beginning of the file, 
which is specified using the whence parameter and is set to 0.

The readlines() method in Python is a function of file objects that reads the 
entire contents of a file and returns it as a list of strings, 
where each element in the list is a single line from the file. '''