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
            font='arial, 25 bold', width=10,bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)
    
def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()
    
if __name__ =="__main__":
    main()