from tkinter import Tk, Menu, Text, messagebox
from tkinter.constants import END
from tkinter.simpledialog import askstring
from os import listdir

# function to get typed text
def getText():
    return text_area.get(1.0, END)

# function to ask if to save file
def askSave():
    if len(getText()) > 1:
        return messagebox.askyesnocancel("Save File", "Do you want to save the existing file?")
    return False

# funtion to create new file
def newFile():
    save_file = askSave()
    if save_file == True:
        if not saveFile():
            return
    elif save_file == None:
        return
    text_area.delete(1.0, END)

# function to open file
def openFile():
    save_file = askSave()
    if save_file == True:
        if not saveFile():
            return
    elif save_file == None:
        return
    file_name = askstring("Open", "Enter filename") + ".txt"
    if file_name not in file_list:
        return messagebox.showerror("File Not Found", f"File with name {file_name} is not found")
    file = open("files/" + file_name, "r+")
    text_area.delete(1.0, END)
    text_area.insert(1.0, file.read())


def saveFile():
    file_name = askstring("Save", "Enter filename")
    if file_name != None:
        file_name += ".txt"
        if file_name in file_list:
            overwrite = messagebox.askyesnocancel("Warning", "A file with this name exists do you want to overwrite it?")
            if overwrite == None:
                return
            elif overwrite == False:
                return saveFile()
        file = open("files/" + file_name, "w")
        file.writelines(getText())
        messagebox.showinfo("Saved", "The file has been saved")
        return True
    return False

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
        save_file = askSave()
        if save_file == True:
            if not saveFile():
                return
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
file.add_command(label = "New File", command = newFile)
file.add_command(label = "Open File", command = openFile)
file.add_command(label= "Save", command = saveFile)
menubar.add_cascade(label = "File", menu = file)
menubar.add_command(label = "Dark Mode", command = darkmode)
menubar.add_command(label = "Exit",  command = exitNotepad)
notepad.config(menu = menubar)

# text widget
text_area = Text(notepad, bg = "#FFF", fg = "#000")
text_area.focus()
text_area.place(relwidth = 1, relheight = 1, relx = 0, rely = 0)

file_list = listdir("files")
dark = False

notepad.mainloop()