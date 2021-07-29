from tkinter import Tk, Menu, Text, messagebox
from tkinter.constants import END


# get typed text
def getText():
    return text_area.get(1.0, END)

# function to toggle darkmode
def darkmode():
    global dark
    dark = not dark
    if dark:
        text_area.config(bg = "#111", fg = "#FFF")
    else:
        text_area.config(bg = "#FFF", fg = "#000")

# function to close notepad
def exitNotepad():
    if messagebox.askyesno("Close Window", "Are you sure you want to exit?"):
        if len(getText()) > 1:
            save_file = messagebox.askyesnocancel("Save File", "Do you want to save the file before exiting?")
            if save_file == True:
                print("save")
                # saveFile()
            elif save_file == None:
                return
        notepad.destroy()

# notepad window setup
notepad = Tk()
notepad.title("Notepad")
notepad.geometry("480x480")
menubar = Menu(notepad)

# menu bar
file = Menu(menubar, tearoff = 0)
file.add_command(label = "New File")
file.add_command(label = "Open File")
file.add_command(label= "Save")
menubar.add_cascade(label = "File", menu = file)
menubar.add_command(label = "Dark Mode", command = darkmode)
menubar.add_command(label = "Exit",  command = exitNotepad)
notepad.config(menu = menubar)

# text widget
text_area = Text(notepad, bg = "#FFF", fg = "#000")
text_area.place(relwidth = 1, relheight = 1, relx = 0, rely = 0)


dark = False

notepad.mainloop()