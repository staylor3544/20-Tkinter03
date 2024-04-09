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
# DONE: 2. (5 pts)
#
#   Now, create two frames in your window.
#
#   Use the grid() method to place them in the window side by side to each
#   other. Both frames should have 5px of padding in all directions.
#
#   Use the configure methods to make these columns and row responsive in all
#   directions. Choose minimum sizes that make sense (no text should be cut
#   off) but the two columns should both have equal weight (so they remain the
#   same relative size to each other).
#
#   Also, place a label in each frame labeling them as Frame A and Frame B and
#   give them different background colors.
#
#   Use the pack() method simply put the label in each frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################
window = tk.Tk()
window.title("Window")

frame_colors = ["#00008B", "#800080"]

frames = []

for i in range(2):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for x in range(2):
        frame = tk.Frame(
            window,
            bg = frame_colors[x],
            relief = "sunken",
            borderwidth = 3,
            )
        frame.grid(row = i, column = x, pady=5, padx=5,)
        frame.grid_columnconfigure(x, weight=1)
        frames.append(frame)

labels = ["Frame A", "Frame B"] 
label_colors = ["#FBCEB1", "#FFFF8F"] 
for y, label_text in enumerate(labels):
    label = tk.Label(
        frames[y], 
        text = label_text,
        bg = label_colors[y]
        )
    label.pack()

window.mainloop()