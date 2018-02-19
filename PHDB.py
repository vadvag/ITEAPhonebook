class PHBase():
    import sqlite3
    DBNAME = 'PhoneBook.sqlite'
    try:
        fi = open(DBNAME,'rb')
    except:
        conn = sqlite3.connect(DBNAME)
        c = conn.cursor()
        c.execute("""CREATE TABLE PhoneBook
                  (abon varchar primary key,
                  phone varchar)""")
        conn.commit()
        c.close()
        conn.close()
    else:
        fi.close()
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()

    def __init__(self):
        print('init')

    def create(self,abon,phone):
        try:
            self.cursor.execute('insert into PhoneBook (abon, phone) values (?,?)',(abon, phone))
            self.db.commit()
        except:
            raise ValueError('%s alredy exist' % abon)

    def read(self, abon):
        c1 = self.cursor.execute('select phone from PhoneBook where abon = ?', (abon,))
        res = c1.fetchone()
        if not res:
            raise ValueError('Name %a is not exist' %abon)
        raise ValueError('%s: %s' % (abon,res[0]))
        #print(c1.fetchone())

    def update(self, abon, phone):
        self.cursor.execute('update PhoneBook set phone=? where abon = ?',(phone, abon))
        self.db.commit()

    def delete(self, abon):
        self.cursor.execute('delete from PhoneBook where abon = ?',(abon,))
        self.db.commit()
