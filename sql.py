import sqlite3

def search(INCI_name="", CAS_no=""):
    conn=sqlite3.connect('test.db')
    cur=conn.cursor()
    cur.execute('select * from test where INCIName=? or CASNo=?', (INCI_name, CAS_no))
    row=cur.fetchall()
    conn.close()
    return row
