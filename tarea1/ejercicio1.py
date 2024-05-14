# registro de datos personales
data={
    'nombres':'',
    'apellidos':'',
    'dni':'',
}

lista=[]
print("Datos personales")
print("------------------")

nombres= input("ingrese sus nombres: ")
apellidos= input("ingrese sus apellidos: ")
dni= input("ingrese su dni: ")

data['nombres']=nombres
data['apellidos']=apellidos
data['dni']=dni

lista.append(data)
print(lista,len(lista))