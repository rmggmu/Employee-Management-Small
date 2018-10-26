import sqlite3


def connect():
    conn=sqlite3.connect("emp")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS emp(emp_name text ,contact integer,"
                " idno integer PRIMARY KEY ,salary integer)")
    conn.commit()
    conn.close()


def add(emp_name,contact,idno,salary):
    conn = sqlite3.connect("emp")
    cur = conn.cursor()
    cur.execute("INSERT INTO emp VALUES(?,?,?,?)",(emp_name,contact,idno,salary))
    conn.commit()
    conn.close()


def delete(idno):
    conn = sqlite3.connect("emp")
    cur = conn.cursor()
    cur.execute("DELETE FROM emp WHERE idno = (?)",(idno,))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("emp")
    cur = conn.cursor()
    cur.execute("SELECT * FROM emp")
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows

def search(idno):
    conn = sqlite3.connect("emp")
    cur = conn.cursor()
    cur.execute("SELECT * FROM emp WHERE idno=(?)",(idno,))
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows

def update(emp_name,contact,idno,salary):
    conn = sqlite3.connect("emp")
    cur = conn.cursor()
    cur.execute("UPDATE emp SET emp_name=?, contact=?, salary=? WHERE idno=?" ,(emp_name,contact,salary,idno))
    conn.commit()
    conn.close()

