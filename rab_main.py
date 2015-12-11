# RAB (Rencana Anggaran Biaya) python 3.5 desktop
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import rabDB

class rabApp:
    """
    Main Program
    """

    def __init__(self, master):

        self.master = master
        self._createGUI()
        self.database = rabDB.rabDB()
        self.master.protocol("WM_DELETE_WINDOW", self._safe_close)

    def _createGUI(self):
        # set lebar dan tinggi windows
        self.master.geometry(
            "{0}x{1}+0+0".format(self.master.winfo_screenwidth() - 20, self.master.winfo_screenheight() - 20))
        program_directory = sys.path[0]
        self.master.iconphoto(True, PhotoImage(file="images\icon_rab.gif"))
        # root Menu
        rMenu = Menu()

        rmf = Menu()
        rmf.add_command(label='New Project', command=self._submit_newproject)
        rmf.add_command(label='Open Project', command=self._submit_openproject)
        # rmf.add_command(label='Save Project')
        rmf.add_command(label='Close', command=self._createGUI)
        rmf.add_command(label='Print')
        rmf.add_command(label='Exit', command=self._safe_close)

        lmf = Menu()
        lmf.add_command(label='List Project', command=self._submit_openproject)
        lmf.add_command(label='List Material', command=self._list_material)
        lmf.add_command(label='List Kategori', command=self._list_category)
        lmf.add_command(label='List Supplier', command=self._clear_newproject)
        lmf.add_command(label='List Unit/Satuan Material', command=self._list_unit)
        lmf.add_command(label='List Tax', command=self._clear_newproject)

        emf = Menu()
        emf.add_command(label='Edit Project', command=self._submit_openproject)
        emf.add_command(label='Edit Material', command=self._edit_material)
        emf.add_command(label='Edit Kategori', command=self._add_category)
        emf.add_command(label='Edit Supplier', command=self._clear_newproject)
        emf.add_command(label='Edit Unit/Satuan Material', command=self._clear_newproject)
        emf.add_command(label='Edit Tax', command=self._clear_newproject)

        rmm = Menu()
        rmm.add_command(label='Tambah Project', command=self._submit_newproject)
        rmm.add_command(label='Tambah Material', command=self._add_material)
        rmm.add_command(label='Tambah Kategori', command=self._add_category)
        rmm.add_command(label='Tambah Supplier', command=self._clear_newproject)
        rmm.add_command(label='Tambah Unit/Satuan Material', command=self._add_unit)
        rmm.add_command(label='Tambah Tax', command=self._clear_newproject)

        rMenu.add_cascade(label="File", menu=rmf)
        rMenu.add_cascade(label="List", menu=lmf)
        rMenu.add_cascade(label="Edit", menu=emf)
        rMenu.add_cascade(label="Tambah ", menu=rmm)
        rMenu.add_cascade(label="Seting", command=self._clear_newproject)
        rMenu.add_cascade(label="Help", command=self._clear_newproject)
        self.master.config(menu=rMenu)

        # configure style of the GUI
        bgcolor = '#D9F3FA'
        ##D4FCCF
        # self.master.configure(background = bgcolor)
        self.master.title(' Software RAB (Rencana Anggaran Biaya) ')
        # self.master.resizable(False, False)
        self.style = ttk.Style()
        self.style.configure('TFrame', background=bgcolor, borderwidth=15, relief='raised')
        self.style.configure('TButton', font=('Arial Black', 12))
        self.style.configure('TLabel', background=bgcolor, font=('Arial Black', 12))
        self.style.configure('Status.TLabel', background=bgcolor, font=('Arial', 12))
        self.style.configure('Result.TLabel', background=bgcolor, font=('Courier', 12))

        # clear windows freame
        self._clear_newproject()

        # create and display header frame with image
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack(side=TOP)
        self.logo = PhotoImage(file="images\logo_rab.gif")
        ttk.Label(self.frame_header, image=self.logo).pack()

        # create and display frame to hold user input newproject or Open Project
        self.frame_input = ttk.Frame(self.master)
        self.frame_input.pack(side=TOP)
        ttk.Button(self.frame_input, text='New Project',
                   command=self._submit_newproject).grid(row=4, column=0, columnspan=2, padx=8, pady=5)
        ttk.Button(self.frame_input, text='Open Project',
                   command=self._submit_openproject).grid(row=4, column=2, columnspan=2, padx=7, pady=5)

    #Project
    def _submit_newproject(self):
        # clear windows freame
        self._clear_newproject()

        # create form input new project
        self.frame_input_np = ttk.Frame(self.master)
        ttk.Label(self.frame_input_np, text="Buat Proyek Baru", font=('Arial Black', 14)).grid(row=0, column=1,
                                                                                               columnspan=3)
        ttk.Label(self.frame_input_np, text="Nama Project").grid(row=2, column=0, sticky='w')
        ttk.Label(self.frame_input_np, text="Nama Pemilik").grid(row=3, column=0, sticky='w')
        ttk.Label(self.frame_input_np, text="Penanggung Jawab").grid(row=4, column=0, sticky='w')
        ttk.Label(self.frame_input_np, text="Lokasi").grid(row=5, column=0, sticky='w')
        ttk.Label(self.frame_input_np, text="Keterangan").grid(row=6, column=0)

        self.name_proj = StringVar()
        self.name_own = StringVar()
        self.name_manage = StringVar()
        self.location = StringVar()
        self.ket = StringVar()

        self.name_proj = ttk.Entry(self.frame_input_np, font='Courier 11', width=65)
        self.name_proj.grid(row=2, column=1, columnspan=2, padx=5)
        self.name_own = ttk.Entry(self.frame_input_np, font='Courier 11', width=65)
        self.name_own.grid(row=3, column=1, columnspan=2, padx=5)
        self.name_manage = ttk.Entry(self.frame_input_np, font='Courier 11', width=65)
        self.name_manage.grid(row=4, column=1, columnspan=2, padx=5)
        self.location = ttk.Entry(self.frame_input_np, font='Courier 11', width=65)
        self.location.grid(row=5, column=1, columnspan=2, padx=5)
        self.keterangan = Text(self.frame_input_np, width=73, height=10)
        self.keterangan.grid(row=6, column=1, columnspan=2, padx=5)

        # create tombol simpan /batal / clear data
        ttk.Button(self.frame_input_np, text="Kosongkan", command=self._empty_newproject, width=10).grid(row=8,
                                                                                                         column=0,
                                                                                                         padx=2, pady=5,
                                                                                                         sticky='e')
        ttk.Button(self.frame_input_np, text="Batal", command=self._createGUI, width=10).grid(row=8, column=2,
                                                                                              padx=2, pady=5,
                                                                                              sticky='w')
        ttk.Button(self.frame_input_np, text="Simpan", command=partial(self._save_newproject, "save"), width=10).grid(
            row=8, column=1,
                                                                                                     padx=2, pady=5)

        self.frame_input_np.pack(side =TOP)

    def _submit_openproject(self):
        # for open exist project
        # clear windows freame
        self._clear_newproject()

        # show input result
        self.frame_show_result = ttk.Frame(self.master)
        #self.frame_show_result.configure(width=980)

        ttk.Label(self.frame_show_result, text="Nama Project").grid(row=0, column=0, padx=10, pady=3)
        ttk.Label(self.frame_show_result, text="Pemilik Project").grid(row=0, column=1, padx=10, pady=3)
        ttk.Label(self.frame_show_result, text="Penanggung Jawab").grid(row=0, column=2, padx=10, pady=3)
        ttk.Label(self.frame_show_result, text="Lokasi").grid(row=0, column=3, padx=10, pady=3)
        # ttk.Label(self.frame_show_result, text="Keterangan").grid(row=0, column=4,padx=10, pady=3)
        ttk.Label(self.frame_show_result, text="Tanggal").grid(row=0, column=4, padx=10, pady=3)
        # ttk.Label(self.frame_show_result, text="Status").grid(row=0, column=6,padx=10, pady=3)
        ttk.Label(self.frame_show_result, text="Edir/Hapus").grid(row=0, column=5, padx=10, pady=3)

        ttk.Label(self.frame_show_result, text="_" * 125, foreground="yellow").grid(row=1, column=0, columnspan=6)

        # show nama tables pada db
        # datatables = list(self.database.show_tables())
        #print (datatables)

        # show data existing project
        dataresult = list(self.database.get_data('project', 'Date DESC', ''))
        #print (datahasil)
        r = 2

        for entry in dataresult:
            if r % 2 == 0:
                colorbg = '#0D06D6'
            else:
                colorbg = '#000000'

            ttk.Button(self.frame_show_result, text=entry['ProjetcName'],
                       command=partial(self._edit_project, entry['Id'])).grid(row=r, column=0, padx=5, pady=3,
                                                                              sticky='w')
            ttk.Label(self.frame_show_result, text=entry['ProjectOwner'], foreground=colorbg).grid(row=r, column=1,
                                                                                                   padx=5, pady=3,
                                                                                                   sticky='w')
            ttk.Label(self.frame_show_result, text=entry['ProjectManager'], foreground=colorbg).grid(row=r, column=2,
                                                                                                     padx=5, pady=3,
                                                                                                     sticky='w')
            ttk.Label(self.frame_show_result, text=entry['ProjectLocation'], foreground=colorbg).grid(row=r, column=3,
                                                                                                      padx=5, pady=3,
                                                                                                      sticky='w')
            # ttk.Label(self.frame_show_result, text=entry['ProjectInfo']).grid(row=r, column=4,padx=5, pady=3, sticky='w')
            ttk.Label(self.frame_show_result, text=time.ctime(float(entry['Date'])), foreground=colorbg).grid(row=r,
                                                                                                              column=4,
                                                                                                              padx=5,
                                                                                                              pady=3,
                                                                                                              sticky='w')
            # ttk.Label(self.frame_show_result, text=entry['Status']).grid(row=r, column=6,padx=5, pady=3, sticky='w')
            ttk.Button(self.frame_show_result, text='Edit/Hapus',
                       command=partial(self._edit_project, entry['Id'])).grid(row=r, column=5, padx=5, pady=3,
                                                                              sticky='w')

            r += 1
        self.frame_show_result.pack(side=TOP)

    def _save_newproject(self, argumen):
        # get data from form
        self.a = self.name_proj.get()
        self.b = self.name_own.get()
        self.c = self.name_manage.get()
        self.d = self.location.get()
        self.e = self.keterangan.get(1.0, 'end')
        #self.f = self.id.get()

        # save to db
        datetime = time.time()
        status = 1

        if argumen == 'save':
            # save to db
            data = [datetime, status, self.a, self.b, self.c, self.d, self.e]
            self.database.insert_data('project', data)
            # show message box
            messagebox.showinfo(title='RAB Software', message='Proyek baru berhasil di buat')

        elif type(argumen) == list and argumen[0] == 'update':
            # update to db
            data = [datetime, status, self.a, self.b, self.c, self.d, self.e, argumen[1]]
            self.database.update_data('project', data)
            # show message box
            messagebox.showinfo(title='RAB Software', message='Proyek  berhasil di update')

        # clear form new project
        # self._clear_newproject()
        self._submit_openproject()

    def _edit_project(self, iddata):
        # edit data project
        #clear windows freame
        self._clear_newproject()

        dataedit = list(self.database.get_data('project', 'id', iddata))

        # load form input
        self.frame_edit = ttk.Frame(self.master)
        ttk.Label(self.frame_edit, text="Edit Proyek", font=('Arial Black', 14)).grid(row=0, column=1,
                                                                                      columnspan=3)
        ttk.Label(self.frame_edit, text="Nama Project").grid(row=2, column=0, sticky='w')
        ttk.Label(self.frame_edit, text="Nama Pemilik").grid(row=3, column=0, sticky='w')
        ttk.Label(self.frame_edit, text="Penanggung Jawab").grid(row=4, column=0, sticky='w')
        ttk.Label(self.frame_edit, text="Lokasi").grid(row=5, column=0, sticky='w')
        ttk.Label(self.frame_edit, text="Keterangan").grid(row=6, column=0)

        self.name_proj = StringVar()
        self.name_own = StringVar()
        self.name_manage = StringVar()
        self.location = StringVar()
        self.ket = StringVar()

        for ve in dataedit:
            self.name_proj = ttk.Entry(self.frame_edit, font='Courier 11', width=65)
            self.name_proj.insert(0, ve['ProjetcName'])
            self.name_proj.grid(row=2, column=1, columnspan=2, padx=5)
            self.name_own = ttk.Entry(self.frame_edit, font='Courier 11', width=65)
            self.name_own.insert(0, ve['ProjectOwner'])
            self.name_own.grid(row=3, column=1, columnspan=2, padx=5)
            self.name_manage = ttk.Entry(self.frame_edit, font='Courier 11', width=65)
            self.name_manage.insert(0, ve['ProjectManager'])
            self.name_manage.grid(row=4, column=1, columnspan=2, padx=5)
            self.location = ttk.Entry(self.frame_edit, font='Courier 11', width=65)
            self.location.insert(0, ve['ProjectLocation'])
            self.location.grid(row=5, column=1, columnspan=2, padx=5)
            self.keterangan = Text(self.frame_edit, width=73, height=10)
            self.keterangan.insert(1.0, ve['ProjectInfo'])
            self.keterangan.grid(row=6, column=1, columnspan=2, padx=5)

        # create tombol simpan /batal / clear data
        update_arg = ['update', iddata]
        del_proj = ['t' + str(iddata), iddata, ve['ProjetcName']]
        ttk.Button(self.frame_edit, text="Update", command=partial(self._save_newproject, update_arg), width=10).grid(
            row=8, column=0, padx=2, pady=5, sticky='e')
        ttk.Button(self.frame_edit, text="Batal", command=self._createGUI, width=10).grid(row=8, column=1, padx=2,
                                                                                          pady=5)
        ttk.Button(self.frame_edit, text="Hapus Project", command=partial(self._del_project, del_proj), width=15).grid(
            row=8, column=2, padx=2, pady=5, sticky='w')
        self.frame_edit.pack(side=TOP)

    def _del_project(self, data):
        # show message box
        ask = messagebox.askyesno(title='RAB Software', message='Yakin Proyek ' + data[2] + ' akan di HAPUS ?')
        if ask == True:
            self._del_table(data[0])
            self._del_row('project', data[1])

            self._clear_newproject()
            self._createGUI()
            # else :
            #   self._edit_project(data[1])

    def _del_table(self, data_table):
        # delete project
        self.database.clear(data_table)

    # Material
    def _list_material(self):
        self._clear_newproject()
        dataresult = list(self.database.get_data('tmaterial', 'ItemName ASC', ''))
        # print(dataresult)

        self.frame_material = ttk.Frame(self.master)
        ttk.Label(self.frame_material, text="List Bahan Material", font=('Arial Black', 16)). \
            grid(row=0, column=0, columnspan=8)
        ttk.Label(self.frame_material, text="Nama Barang"). \
            grid(row=2, column=0, padx=3, pady=3)
        ttk.Label(self.frame_material, text="Kode Barang"). \
            grid(row=2, column=1, padx=3, pady=3)
        ttk.Label(self.frame_material, text="Harga Barang"). \
            grid(row=2, column=2, padx=3, pady=3)
        ttk.Label(self.frame_material, text="Kategori Barang"). \
            grid(row=2, column=3, padx=3, pady=3)
        ttk.Label(self.frame_material, text="Satuan Barang"). \
            grid(row=2, column=4, padx=3, pady=3)
        ttk.Label(self.frame_material, text="Supplier Barang"). \
            grid(row=2, column=5, padx=3, pady=3)
        ttk.Label(self.frame_material, text="Tanggal Update"). \
            grid(row=2, column=6, padx=3, pady=3)
        ttk.Label(self.frame_material, text="Pajak Barang"). \
            grid(row=2, column=7, padx=3, pady=3)
        ttk.Label(self.frame_material, text="_" * 150, foreground="yellow"). \
            grid(row=3, column=0, columnspan=8)
        r = 4
        for entry in dataresult:
            if r % 2 == 0:
                colorbg = '#0D06D6'
            else:
                colorbg = '#000000'

            ttk.Label(self.frame_material, text=entry['ItemName'], foreground=colorbg).grid(row=r, column=0, padx=5,
                                                                                            pady=3, sticky='w')
            ttk.Label(self.frame_material, text=entry['ItemCode'], foreground=colorbg).grid(row=r, column=1, padx=5,
                                                                                            pady=3, sticky='w')
            ttk.Label(self.frame_material, text=entry['ItemPrice'], foreground=colorbg).grid(row=r, column=2, padx=5,
                                                                                             pady=3, sticky='w')
            ttk.Label(self.frame_material, text=entry['CategoryId'], foreground=colorbg).grid(row=r, column=3, padx=5,
                                                                                              pady=3, sticky='w')
            ttk.Label(self.frame_material, text=entry['UnitId'], foreground=colorbg).grid(row=r, column=4, padx=5,
                                                                                          pady=3, sticky='w')
            ttk.Label(self.frame_material, text=entry['SupplierId'], foreground=colorbg).grid(row=r, column=5, padx=5,
                                                                                              pady=3, sticky='w')
            ttk.Label(self.frame_material, text=time.ctime(float(entry['Date'])), foreground=colorbg).grid(row=r,
                                                                                                           column=6,
                                                                                                           padx=5,
                                                                                                           pady=3,
                                                                                                           sticky='w')
            ttk.Label(self.frame_material, text=entry['Tax'], foreground=colorbg).grid(row=r, column=7, padx=5, pady=3,
                                                                                       sticky='w')
            r += 1

        self.frame_material.pack(side=TOP)

    def _add_material(self):
        # Tambah Material
        self._clear_newproject()

        # create form input new project
        self.frame_material = ttk.Frame(self.master)
        ttk.Label(self.frame_material, text="Tambah Bahan Material Baru", font=('Arial Black', 14)). \
            grid(row=0, column=0, columnspan=3)
        ttk.Label(self.frame_material, text="Nama Barang"). \
            grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        ttk.Label(self.frame_material, text="Kode Barang"). \
            grid(row=4, column=0, padx=5, pady=5, )
        ttk.Label(self.frame_material, text="Harga"). \
            grid(row=4, column=1, padx=5, pady=5, )
        ttk.Label(self.frame_material, text="Kategori"). \
            grid(row=6, column=0, padx=5, pady=5, )
        ttk.Label(self.frame_material, text="Satuan"). \
            grid(row=6, column=1, padx=5, pady=5, )
        ttk.Label(self.frame_material, text="Supplier"). \
            grid(row=8, column=0, padx=5, pady=5, )
        ttk.Label(self.frame_material, text="Pajak"). \
            grid(row=8, column=1, padx=5, pady=5, )

        self.ItemName = StringVar()
        self.ItemCode = StringVar()
        self.ItemPrice = StringVar()
        self.CategoryId = StringVar()
        self.UnitId = StringVar()
        self.SupplierId = StringVar()
        self.Tax = StringVar()

        self.ItemName = ttk.Entry(self.frame_material, font='Courier 11', width=25)
        self.ItemName.grid(row=3, column=0, columnspan=3, padx=5)
        self.ItemCode = ttk.Entry(self.frame_material, font='Courier 11', width=25)
        self.ItemCode.grid(row=5, column=0, padx=5)
        self.ItemPrice = ttk.Entry(self.frame_material, font='Courier 11', width=25)
        self.ItemPrice.grid(row=5, column=1, padx=5)

        catresult = list(self.database.get_data('tcategory', 'CategoryName ASC', ''))
        cat = []
        for item in catresult:
            cat.append(item['CategoryName'])
        self.CategoryId = ttk.Combobox(self.frame_material, values=cat)
        self.CategoryId.grid(row=7, column=0, padx=5)

        # self.UnitId =ttk.Entry(self.frame_material, font='Courier 11', width=25)
        unitresult = list(self.database.get_data('tunit', 'UnitName ASC', ''))
        unit = []
        for item in unitresult:
            unit.append(item['BigUnit'])
        self.UnitId = ttk.Combobox(self.frame_material, values=unit)
        self.UnitId.grid(row=7, column=1, padx=5)

        self.SupplierId = ttk.Entry(self.frame_material, font='Courier 11', width=25)
        self.SupplierId.grid(row=9, column=0, padx=5)
        self.Tax = ttk.Entry(self.frame_material, font='Courier 11', width=25)
        self.Tax.grid(row=9, column=1, padx=5)

        # create tombol simpan /batal / clear data
        ttk.Button(self.frame_material, text="Kosongkan", command=self._empty_newproject, width=10). \
            grid(row=11, column=0, padx=2, pady=5, )
        ttk.Button(self.frame_material, text="Simpan", command=partial(self._save_material, "save"), width=10). \
            grid(row=11, column=1, padx=2, pady=5)
        ttk.Button(self.frame_material, text="Batal", command=self._createGUI, width=10). \
            grid(row=11, column=2, padx=2, pady=5, )

        self.frame_material.pack(side=TOP)

    def _edit_material(self):
        self._clear_newproject()

    def _save_material(self, argumen):
        datetime = time.time()
        if argumen == 'save':
            # save to db
            data = [datetime, self.ItemName.get(), self.ItemCode.get(), self.ItemPrice.get(), self.CategoryId.get(),
                    self.UnitId.get(), self.SupplierId.get(), self.Tax.get()]
            self.database.insert_data('tmaterial', data)
            # show message box
            messagebox.showinfo(title='RAB Software', message='Material Baru berhasil di Tambahkan')

        elif type(argumen) == list and argumen[0] == 'update':
            # update to db
            data = [datetime, status, self.a, self.b, self.c, self.d, self.e, argumen[1]]
            self.database.update_data('tmaterial', data)
            # show message box
            messagebox.showinfo(title='RAB Software', message='Proyek  berhasil di update')

        # back to form add material
        self._add_material()

    def _del_material(self):
        self._clear_newproject()

    # Category
    def _list_category(self):
        self._clear_newproject()
        dataresult = list(self.database.get_data('tcategory', 'CategoryName ASC', ''))
        # print(dataresult)

        self.frame_category = ttk.Frame(self.master)

        # self.labelframe.style(fill="both", expand="yes")

        ttk.Label(self.frame_category, text="List Kategori Material", font=('Arial Black', 16)). \
            grid(row=0, column=0, columnspan=3)
        ttk.Label(self.frame_category, text="Nama Kategori"). \
            grid(row=2, column=0, padx=3, pady=3)
        ttk.Label(self.frame_category, text="Nama Sub Kategori"). \
            grid(row=2, column=1, padx=3, pady=3)
        ttk.Label(self.frame_category, text="_" * 125, foreground="yellow"). \
            grid(row=3, column=0, columnspan=3)

        r = 4
        for entry in dataresult:
            if r % 2 == 0:
                colorbg = '#0D06D6'
            else:
                colorbg = '#000000'

            ttk.Label(self.frame_category, text=entry['CategoryName'], foreground=colorbg).grid(row=r, column=0, padx=5,
                                                                                                pady=3, sticky='w')
            ttk.Label(self.frame_category, text=entry['SubCatName'], foreground=colorbg).grid(row=r, column=1, padx=5,
                                                                                              pady=3, sticky='w')
            r += 1

        self.frame_category.pack(side=TOP)

    def _add_category(self):
        self._clear_newproject()

        self.frame_category = ttk.Frame(self.master)
        ttk.Label(self.frame_category, text="Tambah Kategori", font=('Arial Black', 16)). \
            grid(row=0, column=0, columnspan=3)
        ttk.Label(self.frame_category, text="Nama Kategori"). \
            grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(self.frame_category, text="Sub Kategori"). \
            grid(row=3, column=0, padx=5, pady=5, )

        self.CategoryName = StringVar()
        self.SubCatName = StringVar()

        self.CategoryName = ttk.Entry(self.frame_category, font='Courier 11', width=30)
        self.CategoryName.grid(row=2, column=1, padx=5)
        self.SubCatName = ttk.Entry(self.frame_category, font='Courier 11', width=30)
        self.SubCatName.grid(row=3, column=1, padx=5)

        # create tombol simpan /batal / clear data
        ttk.Button(self.frame_category, text="Kosongkan", command=self._empty_newproject, width=10). \
            grid(row=5, column=0, padx=2, pady=5, )
        ttk.Button(self.frame_category, text="Simpan", command=partial(self._save_category, "save"), width=10). \
            grid(row=5, column=1, padx=2, pady=5)
        ttk.Button(self.frame_category, text="Batal", command=self._createGUI, width=10). \
            grid(row=5, column=2, padx=2, pady=5, )

        self.frame_category.pack(side=TOP)

    def _save_category(self, argumen):
        if argumen == 'save':
            # save to db
            data = [self.CategoryName.get(), self.SubCatName.get()]
            self.database.insert_data('tcategory', data)
            # show message box
            messagebox.showinfo(title='RAB Software', message='Kategori berhasil di Tambahkan')

        elif type(argumen) == list and argumen[0] == 'update':
            # update to db
            data = [self.CategoryName.get(), self.SubCatName.get(), argumen[1]]
            self.database.update_data('tcategory', data)
            # show message box
            messagebox.showinfo(title='RAB Software', message='Kategori  berhasil di update')

        # back to form add category
        self._add_category()

    # Unit
    def _list_unit(self):
        self._clear_newproject()
        dataresult = list(self.database.get_data('tunit', 'UnitName ASC', ''))
        # print(dataresult)

        self.frame_unit = ttk.Frame(self.master)

        # self.labelframe.style(fill="both", expand="yes")

        ttk.Label(self.frame_unit, text="List Satuan Material", font=('Arial Black', 16)). \
            grid(row=0, column=0, columnspan=3)
        ttk.Label(self.frame_unit, text="Nama Satuan"). \
            grid(row=2, column=0, padx=3, pady=3)
        ttk.Label(self.frame_unit, text="Satuan Terbesar"). \
            grid(row=2, column=1, padx=3, pady=3)
        ttk.Label(self.frame_unit, text="Satuan Sedang"). \
            grid(row=2, column=2, padx=3, pady=3)
        ttk.Label(self.frame_unit, text="Satuan Kecil"). \
            grid(row=2, column=3, padx=3, pady=3)
        ttk.Label(self.frame_unit, text="Satuan Terkecil"). \
            grid(row=2, column=4, padx=3, pady=3)
        ttk.Label(self.frame_unit, text="_" * 125, foreground="yellow"). \
            grid(row=3, column=0, columnspan=3)

        r = 4
        for entry in dataresult:
            if r % 2 == 0:
                colorbg = '#0D06D6'
            else:
                colorbg = '#000000'

            ttk.Label(self.frame_unit, text=entry['UnitName'], foreground=colorbg).grid(row=r, column=0, padx=5, pady=3,
                                                                                        sticky='w')
            ttk.Label(self.frame_unit, text=entry['BigUnit'], foreground=colorbg).grid(row=r, column=1, padx=5, pady=3,
                                                                                       sticky='w')
            ttk.Label(self.frame_unit, text=entry['MediumUnit'], foreground=colorbg).grid(row=r, column=2, padx=5,
                                                                                          pady=3, sticky='w')
            ttk.Label(self.frame_unit, text=entry['SmallUnit'], foreground=colorbg).grid(row=r, column=3, padx=5,
                                                                                         pady=3, sticky='w')
            ttk.Label(self.frame_unit, text=entry['VerySmallUnit'], foreground=colorbg).grid(row=r, column=4, padx=5,
                                                                                             pady=3, sticky='w')
            r += 1

        self.frame_unit.pack(side=TOP)

    def _add_unit(self):
        self._clear_newproject()

        self.frame_unit = ttk.Frame(self.master)
        ttk.Label(self.frame_unit, text="Tambah Satuan", font=('Arial Black', 16)). \
            grid(row=0, column=0, columnspan=3)
        ttk.Label(self.frame_unit, text="Nama Satuan"). \
            grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(self.frame_unit, text="Satuan Terbesar"). \
            grid(row=3, column=0, padx=5, pady=5, )
        ttk.Label(self.frame_unit, text="Satuan Sedang"). \
            grid(row=4, column=0, padx=5, pady=5, )
        ttk.Label(self.frame_unit, text="Satuan Kecil"). \
            grid(row=5, column=0, padx=5, pady=5, )
        ttk.Label(self.frame_unit, text="Satuan Terkecil"). \
            grid(row=6, column=0, padx=5, pady=5, )

        self.UnitName = StringVar()
        self.BigUnit = StringVar()
        self.MediumUnit = StringVar()
        self.SmallUnit = StringVar()
        self.VerySmallUnit = StringVar()

        self.UnitName = ttk.Entry(self.frame_unit, font='Courier 11', width=30)
        self.UnitName.grid(row=2, column=1, padx=5)
        self.BigUnit = ttk.Entry(self.frame_unit, font='Courier 11', width=30)
        self.BigUnit.grid(row=3, column=1, padx=5)
        self.MediumUnit = ttk.Entry(self.frame_unit, font='Courier 11', width=30)
        self.MediumUnit.grid(row=4, column=1, padx=5)
        self.SmallUnit = ttk.Entry(self.frame_unit, font='Courier 11', width=30)
        self.SmallUnit.grid(row=5, column=1, padx=5)
        self.VerySmallUnit = ttk.Entry(self.frame_unit, font='Courier 11', width=30)
        self.VerySmallUnit.grid(row=6, column=1, padx=5)

        # create tombol simpan /batal / clear data
        ttk.Button(self.frame_unit, text="Simpan", command=partial(self._save_unit, "save"), width=10). \
            grid(row=8, column=0, padx=2, pady=5)
        ttk.Button(self.frame_unit, text="Batal", command=self._createGUI, width=10). \
            grid(row=8, column=1, padx=2, pady=5, )

        self.frame_unit.pack(side=TOP)

    def _save_unit(self, argumen):
        if argumen == 'save':
            # save to db
            data = [self.UnitName.get(), self.BigUnit.get(), self.MediumUnit.get(), self.SmallUnit.get(),
                    self.VerySmallUnit.get()]
            self.database.insert_data('tunit', data)
            # show message box
            messagebox.showinfo(title='RAB Software', message='Satuan berhasil di Tambahkan')

        elif type(argumen) == list and argumen[0] == 'update':
            # update to db
            data = [self.CategoryName.get(), self.SubCatName.get(), argumen[1]]
            self.database.update_data('tunit', data)
            # show message box
            messagebox.showinfo(title='RAB Software', message='Satuan  berhasil di update')

        # back to form add category
        self._add_unit()

    # Supplier


    # Tax

    def _del_row(self, data_table, id):
        # del row record
        self.database.del_row(data_table, id)

    def _clear_newproject(self):
        # self.frame_header.destroy()
        try:
            self.frame_header.destroy()
        except AttributeError:
            pass
        try:
            self.frame_input.destroy()
        except AttributeError:
            pass
        try:
            self.frame_show_result.destroy()
        except AttributeError:
            pass
        try:
            self.frame_input_np.destroy()
        except AttributeError:
            pass
        try:
            self.frame_edit.destroy()
        except AttributeError:
            pass
        try:
            self.frame_material.destroy()
        except AttributeError:
            pass
        try:
            self.frame_category.destroy()
        except AttributeError:
            pass
        try:
            self.frame_unit.destroy()
        except AttributeError:
            pass

    def _empty_newproject(self):
        # project
        try:
            self.name_proj.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.name_own.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.name_manage.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.location.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.keterangan.delete(1.0, 'end')
        except AttributeError:
            pass
        # material
        try:
            self.ItemName.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.ItemCode.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.ItemPrice.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.CategoryId.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.UnitId.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.SupplierId.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.Tax.delete(0, 'end')
        except AttributeError:
            pass
        # category
        try:
            self.CategoryName.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.SubCatName.delete(0, 'end')
        except AttributeError:
            pass
        # Unit
        try:
            self.UnitName.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.BigUnit.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.MediumUnit.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.SmallUnit.delete(0, 'end')
        except AttributeError:
            pass
        try:
            self.VerySmallUnit.delete(0, 'end')
        except AttributeError: pass

    def _safe_close(self):
        """
        This is called when the user closes the GUI.  It ensures the
        database is properly shut down first.
        """
        self.database.close()
        self.master.destroy()

def main():
    root = Tk()
    app = rabApp(root)
    root.mainloop()


if __name__ == "__main__": main()
