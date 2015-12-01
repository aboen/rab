#!/usr/bin/python3
#  RAB (Rencana Anggaran Biaya) python 3.5 desktop

from tkinter import *
from tkinter import ttk
#import newproject

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
    cetaklabel = Label(root,text="Buat Proyek Baru").grid(row=0, column=1, columnspan=2 )
    ProjectName = Label(root,text="Nama Project").grid(row=2, column=0)
    ProjectOwner = Label(root, text="Nama Pemilik").grid(row=3, column=0)
    ProjectPJ = Label(root, text="Penanggung Jawab").grid(row=4, column=0)
    ProjectLokasi = Label(root, text="Lokasi").grid(row=5, column=0)
    ProjectKet = Label(root, text="Keterangan").grid(row=6, column=0)

    EName = Entry(root, width=100).grid(row=2, column=1)
    EOwner = Entry(root, width=100).grid(row=3, column=1)
    EPJ = Entry(root, width=100).grid(row=4, column=1)
    ELokasi = Entry(root, width=100).grid(row=5, column=1)
    EKet = Entry(root, width=100).grid(row=6, column=1)

    save_project = Button(root, text = "Simpan", command=SaveProject, width=10,padx=2, pady=5).grid(row=8, column=1)
    #save_project.grid(row=8, column=2)
    clear_project = Button(root, text = "Kosongkan",  command=ClearProject,  width=10,padx=2, pady=5).grid(row=8, column=2)
    #clear_project.grid(row=8, column=1)
    batal_project = Button(root, text = "Batal",  command=BatalProject,  width=10,padx=2, pady=5).grid(row=8, column=0)
    #batal_project.grid(row=8, column=0)


def OpenProject():
    FirsWindwosLoad(FALSE)
    #global FirsWindows
    #bila di klik tombol atau dari menu Proyek baru
    cetaklabel = Label(root,text="   Open Project            ", pady=15).grid(row=9, column=1, columnspan=2 )

def SaveProject():
     cetaklabel = Label(root,text="   Project Tersimpan      ", pady=15).grid(row=9, column=1,  columnspan=2)

def ClearProject():
     cetaklabel = Label(root,text="   Clear Tersimpan        ", pady=15).grid(row=9, column=1,  columnspan=2)

def BatalProject():
     cetaklabel = Label(root,text=" Batalkan Penyimpanan   ", pady=15).grid(row=9, column=1,  columnspan=2)

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

