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
                            (Id INT PRIMARY KEY NOT NULL, Date TEXT, Status TEXT, ProjetcName TEXT, ProjectOwner TEXT, ProjectManager TEXT,
                            ProjectLocation TEXT, ProjectInfo TEXT)'''.format(self.table))

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
        self.db.execute('''INSERT INTO {} (Date, Status, ProjetcName, ProjectOwner, ProjectManager, ProjectLocation, ProjectInfo)
                                VALUES (?, ?, ?, ?, ?, ?, ?)'''.format(data_table), (datainput))
        self.db.commit()
        """
        Create table for every project
        """

        # lid = self.db.lastrowid
        # datetime = time.time()
        # status  = 1

        table_project = datainput[2]
        # self.db = sqlite3.connect(self.filename)
        # self.db.row_factory = sqlite3.Row
        self.db.execute('''CREATE TABLE IF NOT EXISTS {}
                            (Id INT PRIMARY KEY NOT NULL, Date TEXT,  ProjetcId INT, MaterialId TEXT, Status INT,
                            Info TEXT)'''.format(table_project))

    def get_data(self, data_table, status):
        """
        Get data from table
        """

        cursor = self.db.execute('''SELECT * FROM {} WHERE Status = {}'''.format(data_table, status))
        for row in cursor:
            yield dict(row)

    """
    def _get_status_for_range(self, start, end):

        # get Dates/Statuses that already exist in DB
        cursor = self.db.execute('''SELECT DISTINCT Date, Status FROM {}
                                     WHERE Date BETWEEN {} AND {}'''.format(self.table,
                                                                            start.strftime('%Y%m%d'),
                                                                            end.strftime('%Y%m%d')))
        for row in cursor:
            yield dict(row)

    def _update_data_for_date(self, date, partial):

        # clear out any partial data for this entry
        if partial:
            self.db.execute('DELETE FROM {} WHERE Date={}'.format(self.table, date.strftime('%Y%m%d')))
            self.db.commit()

        try:
            data = lpoWeb.get_data_for_date(date)
        except:
            raise

        for entry in data:
            self.db.execute('''INSERT INTO {} (Date, Time, Status, Air_Temp, Barometric_Press, Wind_Speed)
                                VALUES (?, ?, ?, ?, ?, ?)'''.format(self.table), (entry['Date'].replace("_", ""),
                                                                                   entry['Time'],
                                                                                   entry['Status'],
                                                                                   entry['Air_Temp'],
                                                                                   entry['Barometric_Press'],
                                                                                   entry['Wind_Speed']))
        self.db.commit()
        #self.ambilhasildata = ambildata
    """

    def clear(self):
        """
        Clears out the database by dropping the current table
        """
        self.db.execute('DROP TABLE IF EXISTS {}'.format(self.table))

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
    db.clear()
    db.close()

    # create db for testing
    db = rabDB(filename='test.db', table='Test')

    # verify the db is empty
    if dict(db) != {}:
        print('Error in rabDB test(): Database is not empty')

    # add data for current date
    try:
        db.update_data_for_date(date.teoday(), False)
    except:
        print('ERROR in rabDB.test(): Could not retrieve data for today\n')

    for entry in db:
        print(entry)

    db.close()


# if this module is run as main it will execute the test routine

if __name__ == "__main__": test()
