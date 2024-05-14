import pandas as p
import os
import sqlite3 as cn
import matplotlib.pyplot as plt

def gererarGrafico():
    with cn.connect('./xproyecto_final/final.db') as conn:
           query='select * from lista'
           df = p.read_sql(query, conn)
           fig, ax = plt.subplots(figsize=(10, 6))
           ax.scatter(df['producto'], df['cantidad'], alpha=0.7)
           plt.xlabel('producto')
           plt.ylabel('precio')
           plt.title('Gráfico de Dispersión')
           plt.show()
