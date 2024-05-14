import pandas as p
import os
import sqlite3 as cn

def loadFile():
    files=os.listdir('./xproyecto_final/Data')
    for file in files:
        df=p.read_csv(f"./xproyecto_final/Data/{file}")
        namefile=file.split('.')[0]
        with cn.connect('./xproyecto_final/final.db') as conn:
            df.to_sql(f'{namefile}',con=conn, index=False, if_exists='replace')
        return namefile
