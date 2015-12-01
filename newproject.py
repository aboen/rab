#new project form

def NewProj():
    ProjectName = Label(root,text="Nama Project").grid(row=2, column=0)
    ProjectOwner = Label(root, text="Nama Pemilik").grid(row=3, column=0)
    ProjectPJ = Label(root, text="Penanggung Jawab").grid(row=4, column=0)
    ProjectLokasi = Label(root, text="Lokasi").grid(row=4, column=0)
    ProjectKet = Label(root, text="Keterangan").grid(row=6, column=0)

    EName = Entry(root, width=50).grid(row=2, column=1)
    EOwner = Entry(root, width=50).grid(row=2, column=1)
    EPJ = Entry(root, width=50).grid(row=2, column=1)
    ELokasi = Entry(root, width=50).grid(row=2, column=1)
    EKet = Entry(root, width=50).grid(row=2, column=1)