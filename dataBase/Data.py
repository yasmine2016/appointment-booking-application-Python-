"""
============================
author:YAN GAO
student ID:1995106
============================
"""
import sqlite3
from sqlite3 import Error
from finalProject.appGui.App_User import App_User
from finalProject.appGui.App_Appoint import App_Appoint



def create_user_from_tuple(row):
    return App_User(
        userid = row[0],
        uname=row[1],
        password=row[2],
        fname=row[3],
        lname=row[4],
        age=row[5],
        city=row[6],
        gender=row[7],
        address=row[8]
    )

def create_appoint_from_tuple(row):
    return App_Appoint(
        userid = row[0],
        date=row[1],
        time=row[2],
        doctorname=row[3]
    )


class Data:
    def __init__(self, db):
        self.db = db
        self.conn = None

        try:
            self.conn = sqlite3.connect(self.db)
        except Error as e:
            print("Failed to connect to db", e, sep="\n")
            exit()



    def load_all_appoint(self, uname):

        # get user id
        uid = self.get_userid(uname)
        if uid != 0 and uid != -1:
            try:
                cur = self.conn.cursor()
                cur.execute("SELECT * FROM appointment_list where userId = ? order by date , time;",(uid,))
                rows = cur.fetchall()
                appoint = []
                for row in rows:
                    appoint.append(create_appoint_from_tuple(row))

                return appoint
            except Error as e:
                print("Failed to load appointment_list from db!", e, sep="\n")
                exit()

    def insert_user(self,app_user):
        try:
            cur = self.conn.cursor()
            cur.execute(f"INSERT INTO user  values(?,?,?,?,?,?,?,?,?) ;",
                        (app_user.uid,app_user.uname,app_user.psw,app_user.fname,app_user.lname,app_user.age
                         ,app_user.city,app_user.gender,app_user.addr))
            self.conn.commit()

            return True
        except Error as e:
            print("Failed to insert user table!", e, sep="\n")
            return False

    def insert_appointList(self,app_appoint):
        # check exist
        if self.chk_appoint_exist(app_appoint)==0:
            try:
                cur = self.conn.cursor()
                cur.execute(f"INSERT INTO appointment_list  values(?,?,?,?) ;",
                            (app_appoint.uid,app_appoint.date,app_appoint.time,app_appoint.d_name))
                self.conn.commit()
                return True
            except Error as e:
                print("Failed to insert appointment_list table!", e, sep="\n")
                return False
        elif self.chk_appoint_exist(app_appoint)==1:
            print("The appointment is already exist!(insert_appointList)",sep="\n")
            return False
        else:
            return False

    def check_user(self,u_name,psw):
        try:
            cur = self.conn.cursor()
            cur.execute(f"select * from user where userName = ?;",(u_name,))
            rows = cur.fetchall()
            if rows is not None:
                try:
                    cur = self.conn.cursor()
                    cur.execute(f"select * from user where userName = ? and password = ?;",
                                (u_name, psw))
                    rslt = cur.fetchone()
                    if rslt is not None:
                        return True

                except Error as e:
                    print("Failed to check_user1!", e, sep="\n")
                    return False

        except Error as e:
            print("Failed to check_user2!", e, sep="\n")
            return False

    def show_appointmentInfo(self,app_appoint):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM appointment_list where userId=?;",[app_appoint.uid])
            rows = cur.fetchall()
            appoint = []
            for row in rows:
                appoint.append(create_appoint_from_tuple(row))

            return appoint
        except Error as e:
            print("Failed to load appointment_list from db!", e, sep="\n")
            exit()

    def delete_appointment(self, app_appoint):
        try:
            cur = self.conn.cursor()
            cur.execute(f"DELETE FROM appointment_list WHERE userId = ? and date = ? and time = ?;", (app_appoint.uid,app_appoint.date,app_appoint.time))
            self.conn.commit()

            return True
        except Error as e:
            print("Failed to delete appointment!", e, sep="\n")
            return False

    def update_appointment(self, app_appoint):
        if self.chk_appoint_exist(app_appoint)==0:
            try:
                cur = self.conn.cursor()
                cur.execute("""
                        UPDATE `appointment_list`
                        SET
                            date = ?,
                            time = ?,
                            doctorName = ?,
                        WHERE userId = ?
                        ;""", (
                    app_appoint.date,
                    app_appoint.time,
                    app_appoint.d_name,
                    app_appoint.uid
                ))
                self.conn.commit()

                return True
            except Error as e:
                print("Failed to update_appointment!", e, sep="\n")
                return False
        elif self.chk_appoint_exist(app_appoint)==1:
            print("Appointment is already exist!(update_appointment)", sep="\n")
            return False
        else:
            return False

    def chk_appoint_exist(self, app_appoint):
        try:
            cur = self.conn.cursor()
            cur.execute(f"select * from appointment_list where userId = ? and date = ? and time = ?;", (app_appoint.uid,app_appoint.date,app_appoint.time))
            rows = cur.fetchall()
            if len(rows) !=0:
                return 1
            else:
                return 0
        except Error as e:
            print("Failed to chk_appoint_exist!", e, sep="\n")
            return -1

    def get_userid(self,u_name):
        try:
            cur = self.conn.cursor()
            cur.execute(f"select userId from user where userName = ?;", (u_name,))
            result = cur.fetchone()
            if result is None :
                return 0
            else:
                return result[0]

        except Error as e:
            print("Failed to get_userid!", e, sep="\n")
            return -1

    def check_register_info(self,app_user):
        try:
            cur = self.conn.cursor()

            cur.execute(f"select * from user where userName = ?;", (app_user.uname,))
            result = cur.fetchone()

            if result is None :
                return 0
            else:
                return 1
        except Error as e:
            print("Failed to check_register_info!", e, sep="\n")
            return -1

    def get_maxid(self):
        try:
            cur = self.conn.cursor()
            cur.execute(f"select Max(userId) from user ")
            result = cur.fetchone()
            if result[0] is None:
                return 0
            if result[0] is not None:
                return result[0]

        except Error as e:
            print("Failed to get_maxid!", e, sep="\n")
            return -1

    def get_previous(self,userid):
        try:
            cur = self.conn.cursor()
            cur.execute(f"select * from appointment_list where userId=? order by date,time DESC",(userid,))
            rows = cur.fetchall()
            appoint = []
            for row in rows:
                appoint.append(create_appoint_from_tuple(row))

            return appoint

        except Error as e:
            print("Failed to get_previous!", e, sep="\n")
            exit()

    def get_next(self,userid):
        try:
            cur = self.conn.cursor()
            cur.execute(f"select * from appointment_list where userId=? order by date,time ",(userid,))
            rows = cur.fetchall()
            appoint = []
            for row in rows:
                appoint.append(create_appoint_from_tuple(row))

            return appoint

        except Error as e:
            print("Failed to get_previous!", e, sep="\n")
            exit()