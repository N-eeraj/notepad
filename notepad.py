from tkinter import Tk, Menu, messagebox

def exitNotepad():
    if messagebox.askyesno("Close Window", "Are you sure you want to exit?"):
        notepad.destroy()

notepad = Tk()
notepad.title("Notepad")
notepad.geometry("480x480")
menubar = Menu(notepad)

file = Menu(menubar, tearoff = 0)
file.add_command(label = "New File")
file.add_command(label = "Open File")
menubar.add_cascade(label = "File", menu = file)
menubar.add_command(label = "Exit",  command = exitNotepad)
notepad.config(menu = menubar)

notepad.mainloop()