from tabulate import tabulate
import pandas as pd
import os
clear = lambda: os.system('cls')

def print_tables(db:dict):
    print(10*"-*+*-"+"\n")
    print("Tables:\n")
    for keys, value in db.items():
                print("-> "+keys)
    print("\n"+10*"-*+*-")
    x = input("\n")

def print_table_content(table, tabble_name,db):
        clear()
        if not db.get(tabble_name):
                return False , "Tabel Not Found!"
        df = pd.DataFrame(table)
        print(f"Tabble: {tabble_name}\n")
        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
        x = input("")
        return True , ""
        pass