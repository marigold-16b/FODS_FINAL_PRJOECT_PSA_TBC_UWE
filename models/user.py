from config.settings import *

import pandas as pd

class User :
    def __init__(self, user_id):
        self.user_id = user_id

    def load_users(self) :
        df =  pd.read_csv(user_file, sep="|", names=["id","name","age" ,"gender","address","email","contact"], dtype=str, engine="python", index_col=False)
        df = df.apply(lambda col : col.str.strip())
        return df
    
    def load_passwords(self) :
        return pd.read_csv(passwords_file, sep="|", names=["id", "password"])
    
    def load_grades(self) :
        print()
        print("=" * 24)
        print("======== GRADES ========")
        print("=" * 24)
        print()
        return pd.read_csv(grades_file, sep="|", names=["id", "name", "enroll_year", "current_year", "sem_gpa", "year_gpa"])
    
    def load_eca(self) :
        print()
        return pd.read_csv(eca_file, sep="|", names=["id", "name", "eca", "year"])
    
    def save(self, df, file) :
        df.to_csv(file, sep="|", index=False, header=False)

    def view_profile(self) :
        df = self.load_users()
        print()
        print("=" * 28)
        print("======== MY PROFILE ========")
        print("=" * 28)
        print()
        print(df[df["id"] == self.user_id])