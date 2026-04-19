from config.settings import enrollment_file
from models.student import Student
from models.teacher import Teacher
from models.exam import ExamDept
from models.admin import Administration 
from modules.auth import Authentication

import pandas as pd
  
class System :
    def get_user(self, uid) :
        if uid.startswith("std") :
            return Student(uid)
        elif uid.startswith("thr") :
            return Teacher(uid)
        elif uid.startswith("exm") :
            return ExamDept(uid)
        elif uid.startswith("adn") :
            return Administration(uid)
        
    def enroll(self) :
        print()
        print("=" * 53)
        print("======== WELCOME TO OUR ENROLLMENT INTERFACE ========")
        print("=" * 53)
        print()
        data = [
            input("Enter name : "),
            input("Enter age : "),
            input("Enter gender : "),
            input("Enter address : "),
            input("Enter email : "),
            input("Enter contact : "),
            input("Enter role : ")
        ]

        df = pd.read_csv(enrollment_file, sep="|", names=["name", "age", "gender", "address", "email", "contact", "role"])

        df.loc[len(df)] = data
        df.to_csv(enrollment_file, sep="|", index=False, header=False)

        print()
        print("We have sucessfully listed your data..")
        print("Please, be in touch with our administration..")
        print("You will also recieve an user id and password after you have been accepted..")
        print("Thank You!!")
        print()

    def run(self) :
        while True :
            print("\n1. Login\n2. Get enrolled\n3. Exit")
            opt = input("Enter your option : ")

            if opt == "1" :
                uid = Authentication.login()
                user = self.get_user(uid)
                self.menu(user)
            elif opt == "2" :
                self.enroll()
            elif opt == "3" :
                print("Exited..")
                return
            else : 
                print("Invalid entry..")

    def menu(self, user) :
        while True :
            print("\n1. View profile")

            if isinstance(user, Student) :
                print("2. Update \n3. Grades\n4. ECA\n5. See Analytics")
            elif isinstance(user, Teacher) :
                print("2. View student\n3. See student analytics")
            elif isinstance(user, ExamDept) :
                print("2. View student\n3. See student analytics\n4. Update student\n5. Update grades")
            elif isinstance(user, Administration) :
                print("2. View Student\n3. See student analytics\n4. Add user\n5. Remove user\n6. Enrollments")

            print("0. Logout")

            ch = input("Choice : ")
            if ch == "0" :
                print("Logged out")
                break
            elif ch == "1" :
                user.view_profile()
            elif isinstance(user, Student) :
                if ch == "2" :
                    user.update_profile()
                elif ch == "3" :
                    user.view_grades()
                elif ch == "4" :
                    user.view_eca()
                elif ch == "5" :
                    user.analytics()
            elif isinstance(user, Teacher) :
                if ch == "2" :
                    user.view_std()
                elif ch == "3" :
                    user.analytics()
            elif isinstance(user, ExamDept) :
                if ch == "2" :
                    user.view_std()
                elif ch == "3" :
                    user.analytics()
                elif ch == "4" :
                    user.update_std()
                elif ch == "5" :
                    user.update_grades()
            elif isinstance(user, Administration) :
                if ch == "2" :
                    user.view_std()
                elif ch == "3" :
                    user.analytics()
                elif ch == "4" :
                    user.add_usr()
                elif ch == "5" :
                    user.delete_usr()
                elif ch == "6" :
                    user.view_enrollments()
            else :
                print("Invalid entry..")