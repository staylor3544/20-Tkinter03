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
#   Now, create two different frames with different dimensions (width and
#   height) and different background colors.
#
#   Use the default pack() method to place them in the window.
#
#   Now, modify your code to make these two frames responsive in all
#   directions. Remember that these frames will no longer need a width and
#   height. You should use the fill, side, and expand keywords in your pack
#   method.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################
window = tk.Tk()
window.title("Window")


frame1= tk.Frame(
   window,
   bg = "black",
   relief = "ridge",
   borderwidth = 5
)
frame1.pack(fill = "both", side = "left", expand = True)

frame2= tk.Frame(
   window,
   bg = "grey",
   relief = "groove",
   borderwidth = 5
)
frame2.pack(fill = "both", side = "left", expand = True)

window.mainloop()