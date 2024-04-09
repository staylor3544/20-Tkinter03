import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, create one frame dimensions 200 by 200.
#
#   Use the default pack() method to place it in the window.
#
#   Also, place 3 labels in the frame labeling them as Label A, Label B, and
#   Label C and give them different background colors.
#
#   Use the place() method to place each of these labels at different
#   coordinates such that they do not overlap.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################
window = tk.Tk()
window.title("Window")

frame1= tk.Frame(
   window,
   borderwidth = 5,
   width = 200,
   height = 200
)
frame1.pack()

Label_A = tk.Label(
    frame1, 
    text = "I'm at (0, 0)", 
    bg = "red"
)
Label_A.place(x = 0, y = 0)

Label_B = tk.Label(
    frame1, 
    text = "I'm at (90, 75)", 
    bg = "yellow"
)
Label_B.place(x = 90, y = 75)

Label_C = tk.Label(
    frame1, 
    text = "I'm at (105, 150)", 
    bg = "blue"
)
Label_C.place(x = 105, y = 150)


window.mainloop()