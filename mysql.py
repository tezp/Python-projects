import MySQLdb

try:
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")

    curs = db.cursor()

    curs.execute("select * from Students")

    for row in curs.fetchall():
        print("Name: %s, Address: %s" % (row[1], row[2]))

        
except Exception as e:
    print(e)

