from config.settings import grades_file, user_file

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import ast

class Analytics :
    @staticmethod
    def safe_list(x) :
        try :
            if pd.isna(x) or str(x).strip() == "":
                return []
            x = str(x).strip()

            if not x.startswith("[") :
                x = "[" + x
            
            if not x.endswith("]") :
                x = x + "]"

            return ast.literal_eval(x)
        except Exception :
            print("Error parsing : ", x)
            return []
    

    @staticmethod
    def student_dashboard(sid) :
        df = pd.read_csv(grades_file, sep="|", names=["id", "enroll_year", "program", "current_year", "sem_gpa", "year_gpa"], dtype=str)

        df_users = pd.read_csv(user_file, sep="|", names=["id", "name", "age", "gender", "address", "email", "contact"], dtype=str)

        student = df[df["id"] == sid]

        if student.empty :
            print("Student not found..")
            return
        
        row = student.iloc[0]

        user_row = df_users[df_users["id"] == sid]
        name = user_row.iloc[0]["name"] if not user_row.empty else "Unknown"

        sem_gpa = np.array(Analytics.safe_list(row["sem_gpa"]))
        year_gpa = np.array(Analytics.safe_list(row["year_gpa"]))

        print()
        print("=" * 35)
        print("======== STUDENT ANALYTICS ========")
        print("=" * 35)
        print("ID : ", row["id"])
        print("Name : ", name)
        print("Average GPA : ", np.mean(year_gpa) if len(year_gpa) > 0 else 0)

        if len(sem_gpa) > 0 :
            plt.plot(sem_gpa, marker="o", label="Semester GPA")
        
        if len(year_gpa) > 0 :
            plt.plot(year_gpa, marker="s", label="Year GPA")

        plt.title(f"GPA Trend - {name}")
        plt.xlabel("Semester / Year Index")
        plt.ylabel("GPA")
        plt.legend()
        plt.grid()

        plt.show()
