from datetime import date, datetime, timedelta
from tkinter import messagebox
import sqlite3

class rabDB():
    """
    data base untuk membuat project baru atau membuka project yang sudah di buat
    """

    def __init__(self, **kwargs):

        self.filename = kwargs.get('filename', 'db/rabproyek.db')
        self.table = kwargs.get('table', 'project')

        self.db = sqlite3.connect(self.filename)
        self.db.row_factory = sqlite3.Row
        self.db.execute('''CREATE TABLE IF NOT EXISTS {}
                            (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Date TEXT,
                            Status TEXT,
                            ProjetcName TEXT,
                            ProjectOwner TEXT,
                            ProjectManager TEXT,
                            ProjectLocation TEXT,
                            ProjectInfo TEXT
                            )'''.format(self.table))
        # tabel tmaterial
        self.db.execute('''CREATE TABLE IF NOT EXISTS tmaterial
                            (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Date TEXT,
                            ItemName TEXT,
                            ItemCode TEXT,
                            ItemPrice FLOAT,
                            CategoryId TEXT,
                            UnitId TEXT,
                            SupplierId TEXT,
                            Tax TEXT
                            )''')
        # tabel tcategory
        self.db.execute('''CREATE TABLE IF NOT EXISTS tcategory
                            (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                            CategoryName TEXT,
                            SubCatName TEXT
                            )''')
        # tabel tunit
        self.db.execute('''CREATE TABLE IF NOT EXISTS tunit
                            (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                            UnitName TEXT,
                            BigUnit TEXT,
                            MediumUnit TEXT,
                            SmallUnit TEXT,
                            VerySmallUnit TEXT
                            )''')
        # tabel tsupplier
        self.db.execute('''CREATE TABLE IF NOT EXISTS tsupplier
                            (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                            SupplierName TEXT,
                            upplierAddress TEXT,
                            SupplierCity TEXT,
                            SupplierProvinci TEXT,
                            SupplierZip TEXT,
                            SupplierCP TEXT,
                            SupplierPhone TEXT,
                            SupplierEmail TEXT,
                            SuppilerTax TEXT
                            )''')
        # tabel ttax
        self.db.execute('''CREATE TABLE IF NOT EXISTS ttax
                            (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Tax TEXT
                            )''')

    def __iter__(self):
        """
        Return generator object with dicts of entire DB contents
        """
        cursor = self.db.execute('SELECT * FROM {} ORDER BY Date'.format(self.table))
        for row in cursor:
            yield dict(row)

    def show_tables(self):
        cursor = self.db.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for row in cursor:
            yield dict(row)

    def insert_data(self, data_table, datainput):
        if data_table == 'project':
            cur = self.db.cursor()
            cur.execute('''INSERT INTO {} (Date, Status, ProjetcName, ProjectOwner, ProjectManager, ProjectLocation, ProjectInfo)
                                    VALUES (?, ?, ?, ?, ?, ?, ?)'''.format(data_table), (datainput))

            """
            Create table for every project
            """
            # datetime = time.time()
            table_project = 't' + str(cur.lastrowid)
            self.db.execute('''CREATE TABLE IF NOT EXISTS {}
                                (Id INTEGER PRIMARY KEY AUTOINCREMENT, Date TEXT,  ProjetcId INT, MaterialId TEXT, ItemPrice FLOAT, Status INT,
                                Info TEXT)'''.format(table_project))

        elif data_table == 'tmaterial':
            self.db.execute('''INSERT INTO {} (Date,ItemName,ItemCode,ItemPrice,CategoryId,UnitId,SupplierId,Tax)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''.format(data_table), (datainput))

        elif data_table == 'tcategory':
            self.db.execute('''INSERT INTO {} (CategoryName,SubCatName)
                                    VALUES (?, ?)'''.format(data_table), (datainput))

        elif data_table == 'tunit':
            self.db.execute('''INSERT INTO {} (UnitName, BigUnit, MediumUnit, SmallUnit, VerySmallUnit)
                                    VALUES (?, ?, ?, ?, ?)'''.format(data_table), (datainput))

        self.db.commit()

    def get_data(self, data_table, status, id ):
        """
        Get data from table
        """
        if status == 0:
            cursor = self.db.execute('''SELECT * FROM {} WHERE Status = {}'''.format(data_table, status))
        elif status == 1:
            cursor = self.db.execute('''SELECT * FROM {} WHERE Status = {}'''.format(data_table, status))
        elif status == 'Date DESC' or status == 'Date ASC':
            cursor = self.db.execute('''SELECT * FROM {} ORDER BY {}'''.format(data_table, status))
        elif status == 'id':
            cursor = self.db.execute('''SELECT * FROM {} WHERE Id = {}'''.format(data_table, id))
        elif status == 'ItemName ASC':
            cursor = self.db.execute('''SELECT * FROM {} ORDER BY {}'''.format(data_table, status))
        elif status == 'UnitName ASC':
            cursor = self.db.execute('''SELECT * FROM {} ORDER BY {}'''.format(data_table, status))

        else:
            cursor = self.db.execute('''SELECT * FROM {} '''.format(data_table))

        #return x = cursor
        for row in cursor:
            yield dict(row)

    def update_data(self, data_table, data_value):
        # update data
        self.db.execute('''UPDATE {} SET Date=?, Status=?, ProjetcName=?, ProjectOwner=?, ProjectManager=?,
                                            ProjectLocation=?, ProjectInfo=? WHERE Id=?'''.format(data_table),
                        (data_value))
        self.db.commit()

    def del_row(self, data_table, id):
        self.db.execute('''DELETE from {} where ID= {}'''.format(data_table, id))
        self.db.commit()

    def clear(self, data_table):
        """
        Clears out the database by dropping the current table
        """
        self.db.execute('DROP TABLE IF EXISTS {}'.format(data_table))

    def close(self):
        """
        Safely close down the database
        """
        self.db.close()
        del self.filename


def test():
    """
    A simple test routine
    """
    # create/clear/close to empty db before testing
    db = rabDB(filename='test.db', table='Test')
    db.clear("Test")
    db.close()

    # create db for testing
    db = rabDB(filename='test.db', table='Test')

    # verify the db is empty
    if dict(db) != {}:
        print('Error in rabDB test(): Database is not empty')


    db.close()


# if this module is run as main it will execute the test routine

if __name__ == "__main__": test()
