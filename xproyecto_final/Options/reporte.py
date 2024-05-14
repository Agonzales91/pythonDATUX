import pandas as p
import os
import sqlite3 as cn

def generarReport():
        with cn.connect('./xproyecto_final/final.db') as conn:
           query='select producto, cantidad from lista where cantidad >=40'
           df=p.read_sql(query,conn)
           df.head()
           df.to_csv('./xproyecto_final/reports/listProduct-report.csv')
           print(df.head()) 