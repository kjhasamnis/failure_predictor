from tkinter import Tk, Label, Button, OptionMenu, StringVar
from InputData import InputPage


#Displaying Data upon selection of Machine
def enter():
    selected_machine = variable.get()
    mlabel = Label(root, text= f"\nSelected Machine is: {selected_machine}")
    mlabel.pack()
    if selected_machine == 'CNC Mill':
        label1 = Label(root, text="\n The standard operating conditions are:\nCutting Speed: 1300 RPM\nFeed: 0.19 mm/rev\nDepth of Cut: 0.29mm  ")
        label1.pack()
    elif selected_machine == 'CNC Lathe':
        label1 = Label(root, text="\n The standard operating conditions are:\nCutting Speed: 1200 RPM\nFeed: 0.18 mm/rev\nDepth of Cut: 0.28mm  ")
        label1.pack()
    elif selected_machine == 'CNC Router':
        label1 = Label(root, text="\n The standard operating conditions are:\nCutting Speed: 1200 RPM\nFeed: 0.17 mm/rev\nDepth of Cut: 0.27mm  ")
        label1.pack()
    elif selected_machine == 'Conventional Lathe':
        label1 = Label(root, text="\n The standard operating conditions are:\nCutting Speed: 800 RPM\nFeed: 0.15 mm/rev\nDepth of Cut: 0.25mm  ")
        label1.pack()
    elif selected_machine == 'Drill':
        label1 = Label(root, text="\n The standard operating conditions are:\nCutting Speed: 1200 RPM\nFeed: 0.15 mm/rev\nDepth of Cut: 0.24mm  ")
        label1.pack()
    elif selected_machine == 'Broach':
        label1 = Label(root, text="\n The standard operating conditions are:\nCutting Speed: 700 RPM\nFeed: 0.11 mm/rev\nDepth of Cut: 0.22mm  ")
        label1.pack()
    elif selected_machine == 'Hobbing Machine':
        label1 = Label(root, text="\n The standard operating conditions are:\nCutting Speed: 900 RPM\nFeed: 0.13 mm/rev\nDepth of Cut: 0.23mm  ")
        label1.pack()
    InputPage.input_params() #Calling function to load 2nd GUI
#Creating Main GUI Window
root = Tk()
root.title("Machine Tool Life Predictor")
root.geometry("500x500")
#Welcome Label
welcome_label = Label(root, text="Welcome to the Tool Life Predictor \n").pack()
#Selection Label
selection_label = Label(root, text="Select the Machine on which the operation is going to be performed:\n").pack()
#Dropdown Box
machine_list = ['Select One','CNC Mill','CNC Lathe','CNC Router','Conventional Lathe','Drill','Broach','Hobbing Machine']
variable = StringVar(root)
variable.set(machine_list[0]) # default value
machine_dropbox = OptionMenu(root,variable,*machine_list).pack()
e_label = Label(root, text="\n").pack()
#Enter Button 
enter_button = Button(root, text="Enter", command = enter).pack()
#Executing
root.mainloop()
