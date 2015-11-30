#!/usr/bin/python3
#  RAB (Rencana Anggaran Biaya) python 3.5 desktop

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("RAB Software")
root.geometry("800x600+50+50")

#Pertama kali dijalankan tampilkan tombol New Project dan Open Project

def FirsWindwosLoad(FWL=TRUE):
    global new_project
    global open_project
    if FWL == TRUE :
        new_project = ttk.Button(root, text = "New Project", command=NewProject, width=30)
        new_project.pack(padx=10, pady=20)
        open_project = ttk.Button(root, text = "Open Project",  command=OpenProject,  width=30)
        open_project.pack()
    else:
        new_project.destroy()
        open_project.destroy()

def NewProject():
    FirsWindwosLoad(FALSE)

    #bila di klik tombol atau dari menu Proyek baru
    cetaklabel = Label(root,text="New Project").pack()

def OpenProject():
    FirsWindwosLoad(FALSE)
    global FirsWindows
    #bila di klik tombol atau dari menu Proyek baru
    cetaklabel = Label(root,text="Open Project").pack()


def Main():
    #root Menu
    rMenu = Menu()
    rMenuFile = Menu()
    rMenuFile.add_command(label='New Project', command = NewProject)
    rMenuFile.add_command(label='Open Project', command = OpenProject)
    rMenuFile.add_command(label='Save Project')
    rMenuFile.add_command(label='Close Project')
    rMenuFile.add_command(label='Print')
    rMenuFile.add_command(label='Exit')

    rMenu.add_cascade(label="File",menu=rMenuFile )
    rMenu.add_cascade(label="Edit")
    rMenu.add_cascade(label="Tambah Data")
    rMenu.add_cascade(label="Seting")
    rMenu.add_cascade(label="Help")

    root.config(menu=rMenu)

    #tampilkan hanya pada pertama kali diload
    FirsWindwosLoad(TRUE)

    #loop root
    root.mainloop()


if __name__=='__main__' :

    Main()

