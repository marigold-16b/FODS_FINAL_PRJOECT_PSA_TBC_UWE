from models.user import User as usr
from modules.analytics import Analytics as da
from config.settings import *

class Student(usr) :
    def update_profile(self) :
        df = self.load_users()
        print()
        print("=" * 20)
        print("\nField are as follow : \nid,name,age,gender,address,email,contact\n")
        print()
        print("=" * 20)
        field = input("Field : ")
        if field == "id" :
            print("ID cannot be updated..")
            return
        value = input("Enter new value : ")

        df.loc[df["id"] == self.user_id, field] = value
        self.save(df, user_file)
        print()
        print("=" * 20)
        print(f"{field} field has been updated with new value :  {value}")
        print()
        print("=" * 20)

    def view_grades(self) :
        df = self.load_grades()
        print("=" * 20)
        print()
        print(df[df["id"] == self.user_id])
        print()
        print("=" * 20)

    def view_eca(self) :
        df = self.load_eca()
        print()
        print("=" * 20)
        print(df[df["id"] == self.user_id])
        print()
        print("=" * 20)

    def analytics(self) :
        da.student_dashboard(self.user_id)