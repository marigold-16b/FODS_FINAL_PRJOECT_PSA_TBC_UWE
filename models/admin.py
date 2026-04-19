from models.user import User as usr
from modules.analytics import Analytics as da
from config.settings import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random 
import ast

class Administration(usr) :
    def generate_id(self, role) :
        return role + str(random.randint(100, 999))
    
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
    
    def add_usr(self) :
        role = input("Enter role (std/thr/exm/adn) : ")
        uid = self.generate_id(role)

        data = [
            uid,
            input("Enter name : "),
            input("Enter age : "),
            input("Enter gender : "),
            input("Enter address : "),
            input("Enter email : "),
            input("Enter contact : "),
        ]

        df = self.load_users()
        df.loc[len(df)] = data
        self.save(df, user_file)

        pwd = self.load_passwords()
        pwd.loc[len(pwd)] = [uid, input("Enter password : ")]
        self.save(pwd, passwords_file)

        print(f"Created id : {uid}")

    def delete_usr(self) :
        uid = input("Enter uid : ")
        
        df_users = self.load_users()
        df_users = df_users[df_users["id"] != uid]
        df_users.to_csv(user_file, sep="|", index=False, header=False)

        df_pass = self.load_passwords()
        df_pass = df_pass[df_pass["id"] != uid]
        df_pass.to_csv(passwords_file, sep="|", index=False, header=False)

        df_grades = self.load_grades()
        df_grades = df_grades[df_grades["id"] != uid]
        df_grades.to_csv(grades_file, sep="|", index=False, header=False)

        df_eca = self.load_eca()
        df_eca = df_eca[df_eca["id"] != uid]
        df_eca.to_csv(eca_file, sep="|", index=False, header=False)

    def view_enrollments(self) :
        df = pd.read_csv(enrollment_file, sep="|", names=["name", "age", "gender", "address", "email", "contact", "role"])

        print(df)
        
    def analytics(self) :
        sid = input("Enter student id : ")
        da.student_dashboard(sid)