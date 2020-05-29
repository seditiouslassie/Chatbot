
import sqlite3


class DB:
    def __init__(self, dbname="details.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE INFO(city text, pincode integer, req text, standard text, board text, medium text, subjects text, contact integer, email text, confirm text)"
        self.conn.execute(stmt)
        self.conn.commit()

<<<<<<< HEAD
    def add_item(self, City, Pincode, Req, Standard, Board, Medium, Subjects, Contact, Email, Confirm):
        stmt = "INSERT INTO INFO (city, pincode, req, standard, board, medium, subjects, contact, email, confirm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = (City, Pincode, Req, Standard, Board, Medium, Subjects, Contact, Email, Confirm)
=======
    def add_item(self, City, Pincode, Standard, Board, Medium, Subjects, Number, Email, Req, Confirm):
        stmt = "INSERT INTO INFO (city, pincode, standard, board, medium, subjects, number, email, req, confirm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = (City, Pincode, Standard, Board, Medium, Subjects, Number, Email, Req, Confirm)
>>>>>>> 4996f3ebacbefe82d22895638a9b1bc352ab5994
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text):
        stmt = "DELETE FROM items WHERE description = (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):
        stmt = "SELECT City, Pincode, Standard, Board, Medium, Subjects, Number, Email, Req, Confirm FROM INFO"
        self.conn.execute(stmt)
        
        #return [x[0] for x in self.conn.execute(stmt)]