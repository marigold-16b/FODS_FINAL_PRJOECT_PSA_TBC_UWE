from models.user import User as usr
from modules.analytics import Analytics as da

class Teacher(usr) :
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