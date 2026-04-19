from models.user import User as usr
from modules.analytics import Analytics as da
from config.settings import *

class ExamDept(usr) :
    def update_std(self) :
        sid = input("Enter student id : ")
        df = self.load_users()

        print("=" * 20)
        print("\nField are as follow : \nid,name,age,gender,address,email,contact\n")
        print()
        print("=" * 20)

        field = input("Field : ")
        if field == "id" :
            print("ID cannot be updated..")
            return
        value = input("Enter new value : ")

        df.loc[df["id"] == sid, field] = value
        self.save(df, user_file)

        print()
        print("=" * 20)
        print(f"{field} has been updated with new value :  {value}")
        print()
        print("=" * 20)

    def update_grades(self) :
        sid = input("Enter student id : ")
        df = self.load_grades()

        sem = input("Sem GPA list : ")
        year = input("Year GPA list : ")

        df.loc[df["id"] == sid, "sem_gpa"] = sem
        df.loc[df["id"] == sid, "year_gpa"] = year

        self.save(df, grades_file)

        print()
        print("=" * 20)
        print(f"Semester gpa list has been updated with new value :  {sem}")
        print()
        print(f"Year gpa list has been updated with new value :  {year}")
        print()
        print("=" * 20)

    def view_std(self) :
        def view_std(self) :
            sid = input("Enter student id : ")
            print()
            print("=" * 20)
            print()
            print(self.load_users().query("id == @sid"))
            print()
            print()
            print("=" * 20)
            print()
            print(self.load_grades().query("id == @sid"))
            print()
            print()
            print("=" * 20)
            print()
            print(self.load_eca().query("id == @sid"))
            print()
            print("=" * 20)

    def analytics(self) :
        sid = input("Enter student id : ")
        da.student_dashboard(sid)