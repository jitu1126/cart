class Mydata:
    def show data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="root",database="one")
        cur = conn.cursor()
        qry="select * from sales"
        cur.execute(qry)
        dt = cur.fetchall()
        print(dt)

    def insert data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="root",database="one")
        cur = conn.cursor()
        qry="insert into sales set name='sameer',city='kota',sale=5000"
        cur.execute(qry)
        conn.commit()
        if cur.rowcount>0:
            print(True)
        else:
            print(False)

    def delete data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="root",database="one")
        cur = conn.cursor()
        qry="delete from sales  where name='sameer'"
        cur.execute(qry)
        conn.commit()
        if cur.rowcount>0:
            print(True)
        else:
            print(False)
        
    def update data(self):
    conn = mysql.connector.connect(host="localhost",user="root",password="root",database="one")
    cur = conn.cursor()
    qry="update sales set name='sameer',city='kota',sale=5000 where name='rafik'"
    cur.execute(qry)
    conn.commit()
    if cur.rowcount>0:
        print(True)
    else:
        print(False)



