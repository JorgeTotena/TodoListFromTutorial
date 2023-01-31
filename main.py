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
    
def main():
    # defines the main window of the program
    root = Tk()
    ui = todo(root)
    root.mainloop()
    
if __name__ =="__main__":
    main()