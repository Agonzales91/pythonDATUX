from Options.addFile import *
from Options.reporte import *
from Options.grafico import *

def showOpcions():
    msg="""
     Bienvenido...
     1. Cargar data
     2. Generar reporte de ventas
     3. Mostrar gráfico
     4. Generar una bitácora
     5. Salir"""
    print(msg)
    opcion=int(input('ingrese la opción: '))
    return opcion

def getFuntion(num):
     if num == 1:
          loadFile()
     if num == 2:
          generarReport()
     if num == 3:
          gererarGrafico()
     if num == 4:
          pass

if __name__=='__main__': 
     op = 01
     try:
          while op != 5:
               op = showOpcions()
               getFuntion(op)
     except Exception as e:
          print(e)