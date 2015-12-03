# RAB (Rencana Anggaran Biaya) python 3.5 desktop

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
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
        self.master.geometry("860x640+50+50")

        # root Menu
        rMenu = Menu()
        rMenuFile = Menu()
        rMenuFile.add_command(label='New Project', command=self._submit_newproject)
        rMenuFile.add_command(label='Open Project', command=self._submit_openproject)
        rMenuFile.add_command(label='Save Project')
        rMenuFile.add_command(label='Close Project')
        rMenuFile.add_command(label='Print')
        rMenuFile.add_command(label='Exit')
        rMenu.add_cascade(label="File", menu=rMenuFile)
        rMenu.add_cascade(label="Edit")
        rMenu.add_cascade(label="Tambah Data")
        rMenu.add_cascade(label="Seting")
        rMenu.add_cascade(label="Help")
        self.master.config(menu=rMenu)

        # configure style of the GUI
        bgcolor = '#CCCCFF'
        # self.master.configure(background = bgcolor)
        self.master.title(' Software RAB (Rencana Anggaran Biaya) ')
        # self.master.resizable(False, False)
        self.style = ttk.Style()
        self.style.configure('TFrame', background=bgcolor)
        self.style.configure('TButton', background=bgcolor, font=('Arial Black', 12))
        self.style.configure('TLabel', background=bgcolor, font=('Arial Black', 12))
        self.style.configure('Status.TLabel', background=bgcolor, font=('Arial', 12))
        self.style.configure('Result.TLabel', background=bgcolor, font=('Courier', 12))

        # create and display header frame with image
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack(side=TOP)
        self.logo = PhotoImage(file='logo_rab_ss.gif')
        ttk.Label(self.frame_header, image=self.logo).pack()

        # create and display frame to hold user input newproject or Open Project
        self.frame_input = ttk.Frame(self.master)
        self.frame_input.pack(side=TOP)
        ttk.Button(self.frame_input, text='New Project',
                   command=self._submit_newproject).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        ttk.Button(self.frame_input, text='Open Project',
                   command=self._submit_openproject).grid(row=3, column=2, columnspan=2, padx=5, pady= 5)

    def _submit_newproject(self):
        # for new project
        self.frame_header.destroy()
        self.frame_input.destroy()

        try:
            self.frame_input_np.destroy()
            self.frame_show_result.destroy()
        except AttributeError:
            pass

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
        ttk.Button(self.frame_input_np, text="Kosongkan", command=self._clear_newproject, width=10).grid(row=8,
                                                                                                         column=0,
                                                                                                         padx=2, pady=5,
                                                                                                         sticky='e')
        ttk.Button(self.frame_input_np, text="Batal", command=self._cancel_newproject, width=10).grid(row=8, column=2,
                                                                                                      padx=2, pady=5,
                                                                                                      sticky='w')
        ttk.Button(self.frame_input_np, text="Simpan", command=self._save_newproject, width=10).grid(row=8, column=1,
                                                                                                     padx=2, pady=5)

        self.frame_input_np.pack(side =TOP)

    def _submit_openproject(self):
        # for open exist project
        self.frame_header.destroy()
        self.frame_input.destroy()

        try:
            self.frame_show_result.destroy()
            self.frame_input_np.destroy()
        except AttributeError:
            pass

        # show input result
        self.frame_show_result = ttk.Frame(self.master)
        self.frame_show_result.configure(width=800)

        ttk.Label(self.frame_show_result, text="Nama Project").grid(row=0, column=0, padx=10, pady=3)
        ttk.Label(self.frame_show_result, text="Pemilik Project").grid(row=0, column=1, padx=10, pady=3)
        ttk.Label(self.frame_show_result, text="Penanggung Jawab").grid(row=0, column=2, padx=10, pady=3)
        ttk.Label(self.frame_show_result, text="Lokasi").grid(row=0, column=3, padx=10, pady=3)
        # ttk.Label(self.frame_show_result, text="Keterangan").grid(row=0, column=4,padx=10, pady=3)
        ttk.Label(self.frame_show_result, text="Tanggal").grid(row=0, column=5, padx=10, pady=3)
        # ttk.Label(self.frame_show_result, text="Status").grid(row=0, column=6,padx=10, pady=3)
        garis = "_" * 100
        ttk.Label(self.frame_show_result, text=garis).grid(row=1, column=0, columnspan=6)

        # show nama tables pada db
        # datatables = list(self.database.show_tables())
        # print (datatables)

        # show data existing project
        datahasil = list(self.database.get_data('project', 1))
        # print (datahasil)
        r = 2
        for entry in datahasil:
            ttk.Button(self.frame_show_result, text=entry['ProjetcName']).grid(row=r, column=0, padx=5, pady=3,
                                                                               sticky='w')
            ttk.Label(self.frame_show_result, text=entry['ProjectOwner']).grid(row=r, column=1, padx=5, pady=3,
                                                                               sticky='w')
            ttk.Label(self.frame_show_result, text=entry['ProjectManager']).grid(row=r, column=2, padx=5, pady=3,
                                                                                 sticky='w')
            ttk.Label(self.frame_show_result, text=entry['ProjectLocation']).grid(row=r, column=3, padx=5, pady=3,
                                                                                  sticky='w')
            # ttk.Label(self.frame_show_result, text=entry['ProjectInfo']).grid(row=r, column=4,padx=5, pady=3, sticky='w')
            ttk.Label(self.frame_show_result, text=time.ctime(float(entry['Date']))).grid(row=r, column=5, padx=5,
                                                                                          pady=3, sticky='w')
            # ttk.Label(self.frame_show_result, text=entry['Status']).grid(row=r, column=6,padx=5, pady=3, sticky='w')
            r += r
        self.frame_show_result.pack(side=TOP)

    def _clear_newproject(self):
        self.name_proj.delete(0, 'end')
        self.name_own.delete(0, 'end')
        self.name_manage.delete(0, 'end')
        self.location.delete(0, 'end')
        self.keterangan.delete(1.0, 'end')

    def _save_newproject(self):
        # get data from form
        self.a = self.name_proj.get()
        self.b = self.name_own.get()
        self.c = self.name_manage.get()
        self.d = self.location.get()
        self.e = self.keterangan.get(1.0, 'end')

        # save to db
        datetime = time.time()
        status = 1
        data = [datetime, status, self.a, self.b, self.c, self.d, self.e]
        self.database.insert_data('project', data)

        # clear form new project
        self._clear_newproject()

        # show message box
        messagebox.showinfo(title='RAB Software', message='Proyek baru berhasil di buat')

    def _cancel_newproject(self):
        # self.frame_header.destroy()
        print("cancel")

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
