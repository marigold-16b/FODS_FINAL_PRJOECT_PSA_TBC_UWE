from config.settings import passwords_file
import pandas as pd

class Authentication :
    @staticmethod
    def login() :
        df = pd.read_csv(passwords_file, sep="|", names=["id", "password"])
        attemp = 0
        while attemp <= 2 :
            print()
            print("=" * 33)
            print("======== LOGIN INTERFACE ========")
            print("=" * 33)
            print()
            uid = input("Enter uid : ").strip()
            pwd = input("Enter password : ").strip()
            
            user = df[(df["id"] == uid) & (df["password"] == pwd)]

            if not user.empty :
                return uid
            else : 
                print("Invalid login")

            attemp += 1
            if attemp == 1 :
                print("Last attemp left")
        else :
            print("All attemp failed")
                