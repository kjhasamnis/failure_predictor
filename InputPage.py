from tkinter import Entry
import tkinter as tk 
from ToolLife import theory

#Estimate Button to next window linking function
def esInputs():
    #Getting values from entry boxes
    opSpeed = int(ops.get())
    feedRate = float(fdr.get())
    depth = float(dpt.get())
    #Input Validation
    if (opSpeed > 1300) or (opSpeed < 700) or (feedRate > 0.2) or (feedRate < 0.1) or (depth > 0.3) or (depth < 0.19):
        tk.Label(win, text = "Please enter parameters in limit").pack()
    else:
        theory.page3(int(opSpeed),float(feedRate),float(depth))
#Clear function
def clear_text():
    ops.delete(0,'end')
    dpt.delete(0,'end')
    fdr.delete(0,'end')

def input_params():
    
    global ops,fdr,dpt,win
    #creating new window
    win = tk.Tk()
    
    #modifying window
    win.title("Input Data")
    win.geometry("500x500")
    #Heading
    tk.Label(win, text = "Enter the parameters used for your operation:\n").pack()
    #Operating speed entry
    Op_speed= tk.Label(win, text = "Operating Speed(in RPM):\n[Should be between 700RPM and 1300RPM in multiples of 100]\n")
    Op_speed.pack()
    ops = Entry(win)
    ops.pack()
    #Feed rate entry
    fedrat= tk.Label(win, text = "Feed Rate(in mm/rev):\n[Should be between 0.1 mm/rev and 0.2 mm/rev]\n")
    fedrat.pack()
    fdr = Entry(win)
    fdr.pack()
    #Depth of Cut entry
    dcut = tk.Label(win, text = "Depth of Cut(in mm):\n[Should be between 0.19mm and 0.30mm]\n")
    dcut.pack()
    dpt = Entry(win)
    dpt.pack()
    #Estimate Button
    Estimate = tk.Button(win, text ="Estimate Tool Life", command = esInputs)
    Estimate.pack()
    #Clear Button
    clear_button = tk.Button(win, text="Clear", command=clear_text)
    clear_button.pack()
    #kick off event loop
    win.mainloop()