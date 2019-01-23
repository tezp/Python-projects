import pymysql

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='Tej')
            self.cursor = self.connection.cursor()
        return self.cursor
# connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='Tej')
# cursor = connection.cursor()

class Operations:
    def createTable(self):
        sql = "create table tpk (name varchar(1000) ,address varchar(1000))"
        cursor = Database().connect()
        cursor.execute(sql)

    def insertData(self, name, address):
        self.name = name
        self.address = address
        sql = "INSERT INTO tpk VALUES (%s,%s)"
        data = (self.name, self.address)
        try:
            cursor = Database().connect()
            if cursor.execute(sql, data) == 1:
                print("Inserted data successfully")
                Database().connection.commit()
        except Exception:
            print("Error")
            Database().connection.rollback()

    def updateData(self, name, address):
        self.name = name
        self.address = address
        sql = "UPDATE tpk SET address=%s WHERE name=%s"
        data = (self.address, self.name)
        try:
            cursor = Database().connect()
            if cursor.execute(sql, data) == 1:
                print("Updated data successfully")
                Database().connection.commit()
        except Exception:
            print("Error")
            Database().connection.rollback()

    def selectData(self):
        sql = "SELECT * FROM tpk"
        try:
            cursor = Database().connect()
            cursor.execute(sql)
            records = cursor.fetchall()
            for row in records:
                print("Name : ", row[0])
                print("Address : ", row[1])
        except Exception:
            print("Error")
            Database().connection.rollback()

    def deleteData(self, name):
        self.name = name
        data = (self.name)
        sql = "DELETE FROM tpk WHERE name=%s"
        try:
            cursor = Database().connect()
            if cursor.execute(sql, data) == 1:
                print("Deleted ")
                Database().connection.commit()
        except Exception:
            print("Error")
            Database().connection.rollback()

    def closeConnection(self):
        Database().connection.close()


class Main:
    if __name__ == '__main__':
        print("Data format : (Name,Address)\n1. Insert \n2. Update Address\n3. Show\n4. Delete")
        inputOption = int(input("Select option : "))
        operation = Operations()
        # operation.createTable()
        if inputOption == 1:
            name = str(input("Enter Name : "))
            address = str(input("Enter Address : "))
            operation.insertData(name, address)
        elif inputOption == 2:
            name = input("Enter Name for which you are changing address: ")
            address = input("Enter New Address : ")
            operation.updateData(name, address)
        elif inputOption == 3:
            print("All Details")
            operation.selectData()
        elif inputOption == 4:
            name = input("Enter Name for which you want to delete record: ")
            operation.deleteData(name)
        operation.closeConnection()
